# Reinforcement

# R-2.4
class Flower():
    def __init__(self, name='', petals=0, price=0.0):
        self._name = name
        self._petals = petals
        self._price = price
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_petals(self, petals):
        self._petals = petals

    def get_petals(self):
        return self._petals

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price


# R-2.5, 2.6, 2.7
class CreditCard:
    """ A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """ Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the acount identifier (e.g., '5391 0375 9387 5309)
        limit       credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self): 
        """ Return current balance."""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied."""
        try:
            if price + self._balance > self._limit:  # if charge would exceed limit, 
                return False                         # cannot accept charge
            else:
                self._balance += price
                return True
        except (ValueError):
            print(f'Invalid value: "{price}." price must be a float()')

    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        if amount < 0:
            raise ValueError
        try:
            self._balance -= amount
        except (ValueError):
            print(f'Invalid value: "{amount}." amount must be a float()')


# R-2.8
After modification - range(1, 58) - wallet #3 will go over its limit first (4959/5000)
if __name__ == '__main__':
    wallet = [ ]
    wallet.append(CreditCard('John Bowman', 'California Savings',
                              '5391 0375 9387 5309', 2500) )
    wallet.append(CreditCard('John Bowman', 'California Federal',
                              '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance',
                              '5391 0375 9387 5309', 5000))
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance( ) > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print( )


# R-2.9, 2.10, 2.12, 2.13, 2.14, 2.15
class Vector:
    """ Represent a vector in a multidimensional space. """
    def __init__ (self, d):
        """ Create d-dimensional vector of zeros."""
        from collections.abc import Sequence

        if isinstance(d, int):
            self._coords = [0] * d
        elif issubclass(type(d), Sequence):
            self._coords = list(d)
        else:
            raise TypeError(f"Invalid argument: {d}. d must be of type int or a sequence")

    def __len__ (self):
        """Return the dimension of the vector. """
        return len(self._coords)

    def __getitem__ (self, j):
        """ Return jth coordinate of vector. """
        return self._coords[j]

    def __setitem__ (self, j, val):
        """ Set jth coordinate of vector to given value. """
        self._coords[j] = val

    def __add__ (self, other):
        """ Return sum of two vectors. """
        if len(self) != len(other):                       # relies on len() method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))                        # start with vector of zeros
        for j in range(len(self)): 
            result[j] = self[j] + other[j] 
        return result

    def __sub__(self, other):
        """ Return difference of two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, val):
        """ Return product of a Vector and a scalar or another Vector. """
        if not isinstance(val, (int, Vector)):
            raise TypeError(f"Invalid operand used: {val}")
        else:
            if isinstance(val, int):
                result = Vector(len(self))
                for i in range(len(self)):
                    result[i] = self[i] * val
            else:
                if len(self) != len(val):
                    raise ValueError('dimensions must agree')
                result = []
                for i in range(len(self)):
                    result.append(self[i] * val[i])
                result = sum(result)
            return result

    def __rmul__(self, val):
        """ Return product of a Vector and a scalar. """
        return self * val

    def __neg__(self):
        from copy import deepcopy
        result = deepcopy(self)
        for i in range(len(result)):
            result[i] = -1 * i
        return result

    def __eq__ (self, other):
        """ Return True if vector has same coordinates as other. """
        return self._coords == other._coords

    def __ne__ (self, other):
        """ Return True if vector differs from other. """
        return not self == other                          # rely on existing __eq__ definition

    def __str__ (self):
        """ Produce string representation of vector. """
        return '<' + str(self._coords)[1:-1] + '>'            # adapt list representation
