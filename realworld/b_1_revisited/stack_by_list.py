"""
stack by list
First In Last Out(FILO)

CRUD

Toy example

s = Stack()
s.push(4)
s.push(5)
s.pop()
5

if linkedlist, append O(1), pop O(1)
if double ended queue, append O(1), pop O(1)
"""


class Stack:
    def __init__(self):
        # create
        self.data = []

    def push(self, e):
        # update
        # tc O(1) in general
        # tc O(N) worst case (growing)
        # sc O(1)
        self.data.append(e)
        return self

    def pop(self):
        # delete
        # tc O(1)
        # just drop the last memory block
        return self.data.pop()

    def search(self, e):
        # read
        # linear search
        # tc O(N)
        # sc O(1)
        return e in self.data


s = Stack()
s.push(4)
s.push(5)
assert s.pop() == 5
