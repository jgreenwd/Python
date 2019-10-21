class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last_node = None


    # Add new Node(args) to end of Stack
    def push(self, args):
        # create new node to append to Stack
        node = Node(args)

        # if Stack is empty, assign to head/current/last
        if self.head is None:
            self.head = node
            self.last_node = node

        # else create reference to node from last_node, assign to last_node
        else:
            node.prev_node = self.last_node
            self.last_node = node

        self.size += 1


    # remove last element from Stack & return element value
    def pop(self):
        # if nothing to pop, return None
        if self.size == 0:
            return None
        val = self.last_node.val

        # if prev_node exists, set last_node to prev_node
        if self.last_node.prev_node is not None:
            self.last_node = self.last_node.prev_node
        else:
            self.last_node = None

        self.size -= 1
        # return previous head node value
        return val


    # return value of current_node in Stack
    def peek(self):
        return self.last_node.val


    # return list of Stack contents
    def print(self):
        output = []
        node = self.last_node
        i = 0
        while i < self.size:
            output.insert(0, node.val)
            node = node.prev_node
            i += 1

        return output

class Node:
    def __init__(self, val):
        self.val = val
        self.prev_node = None
