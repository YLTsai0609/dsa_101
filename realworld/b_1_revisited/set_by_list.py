"""
set by list

CRUD

需要可以去重複值 - 要檢查是否有重複

1. 期望的功能為何 - CRUD
2. 舉例 [1,1,2,3] --> 1,2,3
3. CRUD 分別 input, output 是否合適

Create/Read/Update/Delete

	1. 空的? 1個值 多個值

Time Complexity

create : 
	if nothing : O(1)
	if list_of_element (v1) : O(N^2)
		deduplicate list

add 
	_exist : O(N)
	append : O(N) worse case, average case O(1)

read 
	_exist : O(N)

delete
	_exist : O(N)
	delete : O(1)

"""


class CustomSet:
    def _exist(self, e) -> int:
        for idx, val in enumerate(self._data):
            if val == e:
                return idx
        return -1

    def __init__(self, list_of_element=None) -> "self":
        """create set by list"""
        # check duplicates in list
        # construct CustomSet
        self._data = []

    # def __init__(self, list_of_element=None) -> "self":
    #     """V2 create set by list"""
    #     # check duplicates in list
    #     # construct CustomSet
    #     self._data = []

    def add(self, e) -> "self":
        """update values by element"""
        if self._exist(e) < 0:
            self._data.append(e)
        return self

    def read(self, e) -> int:
        """return index of elements, if None, return -1"""
        return self._exist(e)

    def delete(self, e) -> int:
        """return index of element, if None, return -1"""
        idx = self._exist(e)
        if idx >= 0:
            del self._data[idx]
        return idx


s = CustomSet()
s.add(1)
s.add(1)

assert s._data == [1]
assert s.read(1) == 0

s.add(2)
s.add(3)

s.delete(3)
assert s._data == [1, 2]
