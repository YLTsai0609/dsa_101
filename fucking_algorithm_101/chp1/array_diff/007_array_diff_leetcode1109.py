"""
https://leetcode.com/problems/corporate-flight-bookings/
medium
paid question

Naiveloop - tc : O(qN)
DIff - tc : O(q)
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

        assert len(nums) > 0, "non-valid input array"

        self.diff = [None for _ in range(len(nums))]

        self.diff[0] = nums[0]
        for idx in range(1, len(nums)):
            self.diff[idx] = nums[idx] - nums[idx - 1]

        # for debug
        print(self.diff)

    def add(self, index_from: int, index_to: int, val: int) -> Diff:
        self.diff[index_from] += val
        if index_to + 1 < len(self.diff):
            self.diff[index_to + 1] -= val
        return self

    def to_result(self) -> List[int]:
        res = [None for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for idx in range(1, len(self.diff)):
            res[idx] = res[idx - 1] + self.diff[idx]
        return res



class DiffSol:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
        Output: [10,55,45,25,25]
		"""
        raw = [0 for _ in range(n)]
        diff = Diff(raw)
        for bk in bookings:
            index_from, index_to, val = bk
            index_from -= 1 # start from 1
            index_to -= 1
            diff.add(index_from, index_to, val)
        return diff.to_result()



if __name__ == "__main__":
    n = 5
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    # [10,55,45,25,25]
    for c in [DiffSol]:
        _cls = c()
        res = _cls.corpFlightBookings(bookings=bookings, n=n)
        print(res)
