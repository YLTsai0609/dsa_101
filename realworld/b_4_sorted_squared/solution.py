"""
sorted array

nums = [-7, -4, 0, 2, 5, 10]

use double index to get squared sorted result 
"""

from typing import List


def sol(nums: List[int]) -> List[int]:
    """
    double index, 頭跟尾比，尾會是最大的，頭可能平方後會比尾巴大，就必須插在對應位置，同時尾要退後一格

    tc : O(N) 
    sc : O(N) - list

    round 1
        l = 0, r = 5, i = 5
        -7 --> 49
        10 --> 100
        100 比較大，100放在 i 的位置
        [None, None, ..., 100]
        i -= 1
        r -= 1

    round 2
        l = 0, r = 4, i = 4
        49
        5 --> 25
        49 比較大，49 放在 i 的位置
        l += 1
        i -= 1

    [None, None, ... , 49, 100]


    """

    res = [None for _ in range(len(nums))]
    l = 0
    r = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        lsq = nums[l] ** 2
        rsq = nums[r] ** 2
        if lsq >= rsq:
            res[i] = lsq
            l += 1
        else:
            res[i] = rsq
            r -= 1

    return res


print(sol([-7, -4, 0, 2, 5, 10]))
