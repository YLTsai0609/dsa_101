"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
medium
"""

import random
from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass

class PreSum:
    def __init__(self, matrix : List[List[int]]):
        """
        matrix = [
            [1,2,3],
            [4,5,6]
        ]
        """
        height = len(matrix) # 2
        width = len(matrix[0]) # 3
        self.presum_matrix : List[List[int]] = [
            [None for w in range(width + 1)]
            for h in range(height + 1)
        ]
        # zero padding
        for w in range(width + 1):
            self.presum_matrix[0][w] = 0
        for h in range(height + 1):
            self.presum_matrix[h][0] = 0 

        # w, h = 1, 1
        # presum = [
        #     [0,0,0,0]
        #     [0,1,3,6],
        #     [0,5,12,21]
        # ]
        for w in range(1, width + 1):
            for h in range(1, height + 1):
                self.presum_matrix[h][w] = (
                    self.presum_matrix[h - 1][w] + 
                    self.presum_matrix[h][w - 1] + 
                    matrix[h-1][w-1] - 
                    self.presum_matrix[h-1][w-1]
                    )
        # debugging
        for h in range(height + 1):
            print(self.presum_matrix[h])

    def sumRegion(
        self, height_from: int, width_from: int, height_to: int, width_to: int
    ) -> int:
        return (
            self.presum_matrix[height_to + 1][width_to + 1] - 
            self.presum_matrix[height_to + 1][width_from] -
            self.presum_matrix[height_from][width_to + 1] + 
            self.presum_matrix[height_from][width_from]
        )


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6]
      ]
    # debugging
    PreSum(matrix)

    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    q1 = [2, 1, 4, 3]  # res=8
    q2 = [1, 1, 2, 2]  # res = 11
    q3 = [1, 2, 2, 4]  # res = 12
    for c in [PreSum]:
        _cls = c(matrix=matrix)
        for q in [q1, q2, q3]:
            res = _cls.sumRegion(
                height_from=q[0], width_from=q[1], height_to=q[2], width_to=q[3]
            )
            print(res)
