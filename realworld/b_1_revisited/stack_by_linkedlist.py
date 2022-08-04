class _Node:
    __slot__ = "_element", "_next"

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next


class StackLinked:
    def __init__(self) -> None:
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e


s = StackLinked()
s.push(4)
s.push(5)
assert s.pop() == 5
