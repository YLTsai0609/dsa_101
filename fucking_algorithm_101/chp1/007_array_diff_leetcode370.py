"""
https://leetcode.com/problems/range-addition/
medium
paid question

Naiveloop - tc : O(qN)
DIff - tc : O(q)
"""


from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


class Diff:
    def __init__(self, nums: List[int]) -> None:

        assert len(nums) > 0, "non-valid input array"

        self.diff = [None for _ in range(len(nums))]

        self.diff[0] = nums[0]
        for idx in range(1, len(nums)):
            self.diff[idx] = nums[idx] - nums[idx - 1]

        # for debug
        print(self.diff)

    def add(self, index_from: int, index_to: int, val: int) -> None:
        self.diff[index_from] += val
        if index_to + 1 < len(self.diff):
            self.diff[index_to + 1] -= val

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
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    # [-2,0,3,5,3]
    for c in [DiffSol]:
        _cls = c()
        res = _cls.getModifiedArray(length=length, updates=updates)
        print(res)
