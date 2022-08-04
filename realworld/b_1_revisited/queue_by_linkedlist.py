"""
First in first out (FIFO)
CRUD


q = Queue()
q.push(5)
q.push(4)
q.pop()
5

analysis of enqueue, dequeue

enqueue, append node to linked list (we use front(head), rare(tail)) 2 index
tc O(1)
sc O(1)

dequeue, first out, remove the first (we use front(head), rare(tail)) 2 index
tc O(1)
sc O(1)
"""


class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueueLinked:
    def __init__(self) -> None:
        # create
        self._front = None
        self._rare = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        # update
        # double index
        # insert to tail O(1)
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    def dequeue(self):
        """
		delete
		take out the frist, 
		tc O(1)
		"""
        if self.is_empty():
            print("Queue is Empty")
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        self._rare = None
        return e

    def display(self):
        p = self._front
        while p:
            print(p._element, end="<--")
            p = p._next
        print()

    def search(self, e):
        """
		tc O(N)
		sc O(1)
		"""
        p = self._front
        idx = 0
        while p:
            if p._element == e:
                return idx
            idx += 1
            p = p._next
        return -1


q = QueueLinked()
q.enqueue(4)
q.enqueue(5)
q.enqueue(8)
q.display()
assert q.dequeue() == 4
print(q.search(10), q.search(5))
