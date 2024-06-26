"""
https://leetcode.com/problems/range-addition/
medium
paid question

場景釐清
length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]

長度最大會到多少呢? --> 是否會出現大數?
所以可以假設 updates 的三元組, i, j, k  皆為自然數， 0~N, k 為任意整數，對嗎



Naiveloop - tc : O(qN)
    每一個 updates, 都針對 i, k 進行操作，query 次數為 q, 每次 max - min 平均為 N
    tc : O(qN)
    sc : O(1)
DIff - tc : O(q)
    建立一個差分數組，diff, 只需要對 diff[i], diff[j+1] 加減，最後做還原
    tc : O(q)
    sc : O(1)


"""


from __future__ import annotations
from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


class Diff:
    def __init__(self, nums: List[int]) -> None:
        """
        length = 5
        updates = [[1,3,2]]
        out = [0,2,2,2,0]
        """

        assert len(nums) > 0, "non-valid input array"
        self.diff = [None for _ in range(len(nums))]
        self.diff[0] = nums[0]
        for idx in range(1, len(nums)):
            self.diff[idx] = nums[idx] - nums[idx - 1]
        print(self.diff)

    def add(self, index_from : int, index_to : int, val : int) -> Diff:
        self.diff[index_from] += val
        # only if valid array index
        if index_to +1 < len(self.diff):
            self.diff[index_to + 1 ] -= val

        return self
    
    def to_result(self) -> List[int]:
        res = [None for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for idx in range(1, len(self.diff)):
            res[idx] = res[idx - 1] + self.diff[idx]
        return res



class DiffSol:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
		Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
		Output: [-2,0,3,5,3]
		"""
        raw = [0 for _ in range(length)]
        diff = Diff(raw)
        for upd in updates:
            index_from, index_to, val = upd
            diff.add(index_from, index_to, val)
        return diff.to_result()
        



if __name__ == "__main__":
    # unit test
    assert Diff([0,0,0,0,0]).add(1,3,2).to_result() == [0,2,2,2,0]

    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    # [-2,0,3,5,3]
    for c in [DiffSol]:
        _cls = c()
        res = _cls.getModifiedArray(length=length, updates=updates)
        print(res)
