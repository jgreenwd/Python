## building a Queue for practice

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last_node = None


    # Add new Node(args) to end of Queue
    def enqueue(self, args):
        # create new node to append to Queue
        node = Node(args)

        # if Queue is empty, assign to head/last
        if self.head is None:
            self.head = node
            self.last_node = node

        # else move reference to node from last_node, assign to last_node
        else:
            self.last_node.next_node = node
            self.last_node = node

        self.size += 1


    # remove head element from Queue & return element value
    def dequeue(self):
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


    # return value of current_node in Queue
    def peek(self):
        return self.head.val

    def print(self):
        node = self.head
        i = 0
        while i < self.size:
            print(node.val, i)
            node = node.next_node
            i += 1

class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None
