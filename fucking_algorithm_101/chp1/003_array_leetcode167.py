"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
medium

需求釐清

1. 如果有重複的元素，例如[1,1]，兩個都可以被使用到嗎
2. 會不會有 nums 的元素全部相加都不會等於 target 的情況，這種情況下需要回傳什麼才滿足需求?
3. list 中的元素是否全部都是數值，且不會有超大數?

"""

from operator import le
from typing import List


def nested_loop(nums: List[int], target: int) -> List[int]:
    """
    tc : O(N^2)
    sc : O(1)
    """
    for i1, e1 in enumerate(nums):
        for i2, e2 in enumerate(nums):
            if e1 + e2 == target:
                return [i1 + 1, i2 + 1]
    return [-1, -1]


def hash_table_sol(nums: List[int], target: int) -> List[int]:
    """
    tc : O(N)
    sc : O(N)
    """
    h = {val: idx for (idx, val) in enumerate(nums)}
    for i1, e1 in enumerate(nums):
        e2 = target - e1
        if e2 in h.keys():
            i2 = h[e2]
            return [i1 + 1, i2 + 1]
    return [-1, -1]


def twopointer_sol(nums: List[int], target: int) -> List[int]:
    """
    sc : O(1)
    tc : O(N)
    use sorted condition
    """
    # 雙指標，相向而行
    left = 0
    right = len(nums) - 1

    while right > left:
        _sum = nums[left] + nums[right]
        if _sum == target:
            return [left + 1, right + 1]
        elif _sum > target:
            # _sum 必須變小，因為已經排序好了，所以變小的方法就是
            right -= 1
        elif _sum < target:
            left += 1
    return [-1, -1]


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [2, 7, 11, 15]
    target2 = 100
    for nums, target in [(nums1, target1), (nums2, target2)]:
        for func in [nested_loop, hash_table_sol, twopointer_sol]:
            print(func(nums, target))
