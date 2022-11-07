"""
presum for check student score distribution
"""

from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


class PreSum:
    def __init__(self, scores: List[int]):
        """
        sc : O(1) , score buckets fix at 101 buckets, which represents 0 ~ 100
        tc : O(N), N for numbers of sutdents
        scores :  [100, 30, 90]
        """

        # [0, 0, ..., 1, ..., 1, ... 0, 1]
        self.score_dist = [0 for _ in range(101 + 1)]  # socre = 0 ~ score = 100
        self.dist_presum = [None for _ in range(101 + 1)]

        for s in scores:
            self.score_dist[s] += 1

        self.dist_presum[0] = 0
        for i in range(1, 101 + 1):
            # [0, 2, 7, 8]
            self.dist_presum[i] = self.dist_presum[i - 1] + self.score_dist[i - 1]
        # for debug
        print(self.dist_presum)

    def sumRange(self, left: int, right: int) -> int:
        # q = [0, 1], res = 7
        # q = [1, 2], res = 6
        # q = [0, 2], res = 8
        return self.dist_presum[right + 1] - self.dist_presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    scores = [100, 30, 90]
    q1 = [0, 29]  # res = 0
    q2 = [0, 50]  # res = 1
    q3 = [0, 100]  # res = 3
    q4 = [30, 31]  # res = 1
    for c in [PreSum]:
        _cls = c(scores=scores)
        for q in [q1, q2, q3, q4]:
            res = _cls.sumRange(left=q[0], right=q[1])
            print(res)
