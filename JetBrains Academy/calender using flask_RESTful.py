import datetime
import sys
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
db.create_all()


# SQLAlchemy: Event model for interfacing with DB
class EventDB(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


# Resource/Api: Resource model for response processing
class EventsBase(Resource):
    RESOURCE_FIELDS = {'id': fields.Integer, 'event': fields.String, 'date': fields.DateTime('iso8601'), 'message': fields.String}


class Events(EventsBase):
    @marshal_with(EventsBase.RESOURCE_FIELDS)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_time', type=inputs.date, help='Required event date format: YYYY-MM-DD')
        parser.add_argument('end_time', type=inputs.date, help='Required event date format: YYYY-MM-DD')

        args = parser.parse_args()

        if (start := args['start_time']) is not None and (end := args['end_time']) is not None:
            start, end = start.date(), end.date()
            return EventDB.query.filter(start <= EventDB.date, EventDB.date <= end).all()

        return EventDB.query.all()

    @marshal_with(EventsBase.RESOURCE_FIELDS)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('event', type=str, required=True, help='The event name is required!')
        parser.add_argument('date', type=inputs.date, required=True,
                            help='The event date with the correct format is required! The correct format is YYYY-MM-DD!')

        args = parser.parse_args()

        db.session.add(EventDB(event=str(args['event']), date=inputs.date(str(args['date'].date()))))
        db.session.commit()

        return {'event': args['event'], 'date': args['date'].date(), 'message': 'The event has been added!'}


class EventsToday(EventsBase):
    @marshal_with(EventsBase.RESOURCE_FIELDS)
    def get(self):
        return EventDB.query.filter(EventDB.date == datetime.date.today()).all()


class EventsByID(EventsBase):
    @staticmethod
    def _get_event_by_id(event_id):
        event = EventDB.query.filter(EventDB.id == event_id).first()
        if not event:
            abort(404, "The event doesn't exist!")
        return event

    @marshal_with(EventsBase.RESOURCE_FIELDS)
    def get(self, event_id):
        return EventsByID._get_event_by_id(event_id)

    @marshal_with(EventsBase.RESOURCE_FIELDS)
    def delete(self, event_id):
        event = EventsByID._get_event_by_id(event_id)

        db.session.delete(event)
        db.session.commit()

        return {'message': 'The event has been deleted!'}


api.add_resource(Events, '/event')
api.add_resource(EventsToday, '/event/today')
api.add_resource(EventsByID, '/event/<int:event_id>')


# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
