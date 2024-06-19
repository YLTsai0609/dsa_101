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
modified in place

idea 1 : 因為是排序好的，所以重複值必定在 index 上會相臨
可以用雙指針
一次指向兩個來比較，並且用一個 counter 維護目前有幾個獨立值
"""

# O(N^2)
# "in" 

from typing import List

# # [0,1,2]
# def list_remove(nums: List[int],mark='*') -> List[int]:
#     # 0
#     # 1 ~ N
#     # 1
#     # 2 ~ N
#     for i in range(len(nums) - 1):
#         for j in range(i+1, len(nums)):
#             if nums[j] == nums[i]:
#                 # nums.remove(nums[j]) # remove duplicates, 但是就變小了，所以必須用取代的
#                 nums[j] = mark
#     #             # j as fast, i as slow
#     # 這個做法，必定要 new 新的 array
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


def remove_duplicates_in_place(nums : List[int]) -> int:
    '''
    nums = [0,1,1,2], return 3
    
    # 快慢指針，快指針先走，遇到快慢相同 (duplicates)， skip
    # 遇到快慢不同， nums[slow] 直接被取代
    # return nums[:slow]
    '''
    fast = 0
    slow = 0

    # fast = 0, slow = 0 skip
    # fast = 1, slow = 0 --> slow = 1, nums = [0,1,1,2]
    # fast = 2, slow = 1 skip
    # fast = 3, slow = 1 --> slow = 2, nums = [0,1,2,2]

    while fast < len(nums):
        if nums[fast] != nums[slow]:
            # find unique, in-place modifiy
            slow += 1
            nums[slow] = nums[fast]
        # skip
        fast +=1
    return slow + 1

def remove_duplicates(nums : List[int]) -> int:
    '''
    nums = [0,1,1,2], return 3
    # tc : O(N)
    # sc : O(1)
    '''

    slow = 0
    fast = 0
    
    # iteration 0
    # fast = 0, slow = 0, nums = [0]
    # iter 1
    # fast = 1, slow = 1, nums = [0,1]
    # iter 2, fast = 1, slow = 1 --> fast = 2 "SKIP"
    # iter 3, fast = 2 slow = 2 --> fast = 3, nums = [0,1,2]
    # 快指針先走
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            # 獨立值
            slow =+ 1
            nums[slow] = nums[fast]
            # 重複值
        fast += 1
    # nums[:slow]
    return slow + 1

if __name__ == "__main__":
    nums1 = [1, 1, 2] # 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] # 5
    for func in [with_new_array, remove_duplicates_in_place]:
        print(
            func(nums1),
              func(nums2)
            )
