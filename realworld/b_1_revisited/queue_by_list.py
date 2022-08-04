"""
First in first out (FIFO)
CRUD


q = Queue()
q.push(5)
q.push(4)
q.pop()
5
"""


class Queue:
    def __init__(self) -> None:
        # create
        self.data = []

    def push(self, e):
        # update v1
        # append --> tc O(1), pop --> tc O(N)

        # update v2
        # insert --> tc O(N), pop --> tc O(1)

        # update v3
        # linked list version with front, rare (queue)
        self.data.append(e)

    def pop(self):
        # remove from first
        # tc O(N), all of them should move
        return self.data.pop(0)

    def search(self, e):
        # tc O(N)
        return e in self.data  # return bool
        # return self.data.index(e) # return first index from left to right


q = Queue()
q.push(5)
q.push(4)
assert q.pop() == 5
