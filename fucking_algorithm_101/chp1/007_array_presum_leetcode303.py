"""
https://leetcode.com/problems/range-sum-query-immutable/
easy
"""

from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


class PreSum:
    def __init__(self, nums: List[int]):
        # [2, 5, 1]
        n = len(nums)
        self.presum = [None for _ in range(n + 1)]
        self.presum[0] = 0

        for i in range(1, n + 1):
            # [0, 2, 7, 8]
            self.presum[i] = self.presum[i - 1] + nums[i - 1]
        # for debug
        print(self.presum)

    def sumRange(self, left: int, right: int) -> int:
        # q = [0, 1], res = 7
        # q = [1, 2], res = 6
        # q = [0, 2], res = 8
        return self.presum[right + 1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    q1 = [0, 2]  # res = 1
    q2 = [2, 5]  # res = -1
    q3 = [0, 5]  # res = -3
    for c in [PreSum]:
        _cls = c(nums=nums)
        for q in [q1, q2, q3]:
            res = _cls.sumRange(left=q[0], right=q[1])
            print(res)
