## incomplete

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.current_node = None
        self.last_node = None


    # Add new Node(args) to end of DoublyLinkedList
    def push(self, args):
        # create new node to append to DoublyLinkedList
        node = Node(args)

        # if DoublyLinkedList is empty, assign to head/current/last
        if self.head is None:
            self.head = node
            self.current_node = node
            self.last_node = node

        # else move reference to node from last_node, assign to last_node
        else:
            self.last_node.next_node = node
            self.last_node = node

        self.size += 1


    # remove head element from LinkedList & return element value
    def pop(self):
        # if nothing to pop, return None
        if self.size == 0:
            return None
        val = self.head.val

        # if next_node exists, set head to next_node
        if self.head.next_node is not None:
            self.head = self.head.next_node
        else:
            self.head = None

        self.size -= 1
        # return previous head node value
        return val


    # return value of current_node in DoublyLinkedList
    def peek(self):
        return self.current_node.val


    # move to next_node in DoublyLinkedList
    def next(self):
        self.current_node = self.current_node.next_node
        return self.current_node

    # move to prev_node in DoublyLinkedList
    def prev(self):
        self.current_node = self.current_node.prev_node
        return self.current_node

    # return list of DoublyLinkedList contents
    def print(self):
        output = []
        node = self.head
        i = 0
        while i < self.size:
            output.append(self.next())
            i += 1

        return output


class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.prev_node = None
