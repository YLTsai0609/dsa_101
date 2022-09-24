"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
easy
no extra space for another array, modifiying the input array in-place

nums = [1,1,2]
out : 2, nums = [1,2, _]

nums = [0,0,1,1,1,2,2,3,3,4]
out : 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums 的長度限制在 1, 3 * 10^4 之間
-100 <- num[i] <= 100
"""

"""
idea 1 : 因為是排序好的，所以重複值必定在 index 上會相臨，可以用雙指針，一次指向兩個來比較，並且用一個 counter 維護目前有幾個獨立值
"""

from typing import List


# def remove_in_array(nums: List[int]) -> List[int]:
#     """
#     [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#     """
#     if len(nums) == 0:
#         return []
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         if nums[slow] == nums[fast] and slow == fast:
#             fast += 1
#         elif nums[slow] == nums[fast]:
#             nums.remove(fast)  # O(N)
#         elif nums[slow] != nums[fast]:
#             # find unique
#             slow = fast  # jump over the duplicates
#             fast += 1
#     return nums


def with_new_array(nums: List[int]) -> List[int]:
    """
    # create new array
    sc : O(N)
    tc : O(N)
    # using list.remove
    sc : O(1)
    tc : O(N^2)
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    """
    if len(nums) == 0:
        return []
    deduplicates = []
    slow = 0
    fast = 0
    deduplicates.append(nums[slow])
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            # find unique
            slow = fast  # jump over the duplciates
            deduplicates.append(nums[fast])
        fast += 1
    return deduplicates


def remove_deuplicates(nums: List[int]) -> int:
    """
    sc : O(1)
    tc : O(N)
    """
    if len(nums) == 0:
        # return []
        return 0
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    # return nums[:slow + 1]
    return slow + 1


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    for func in [with_new_array, remove_deuplicates]:
        print(func(nums1), func(nums2))
