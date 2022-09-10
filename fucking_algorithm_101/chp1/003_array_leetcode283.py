"""
https://leetcode.com/problems/move-zeroes/

"""

from typing import List


def with_new_array(nums: List[int]) -> List[int]:
    rearranged = []
    n_zeros = 0
    for e in nums:
        if e != 0:
            rearranged.append(
                e
            )  # almost contant, but it might be O(N) when copy all element to new array
        else:
            n_zeros += 1

    for _ in range(n_zeros):
        rearranged.append(0)
    return rearranged


def slow_fast(nums: List[int]) -> List[int]:
    """
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    fast, slow
    tc O(N)
    sc O(1)
    # inplace delete, 所以其實是 slicing
    # 遇到 0 跳過(快指針)
    # 非 0 assign 給慢指針 
    """
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0:
            # keep traverse
            pass
        else:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    for func in [with_new_array, slow_fast]:
        print(func(nums1))
