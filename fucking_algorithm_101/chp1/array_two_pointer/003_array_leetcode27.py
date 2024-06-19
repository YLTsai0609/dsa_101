"""
https://leetcode.com/problems/remove-element/solution/
easy
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    * 要 inplace delete, 所以不會真的 delete，而是用 slicing 來解，也就是說遇到 val 要跳過
    * 快慢指針，快指針遇到 val 就繼續走
    * 遇到不等於 val，就放到慢指針，最後 slicing array
    * tc : O(N)
    * sc : O(1)
    """
    slow = 0
    fast = 0
    # target val = 2
    # iter 1, fast = 0, slow = 0, nums = [0]
    # iter 2, fast = 1, slow = 1, nums = [0,1]
    # iter 3, fast = 2 (hit), slow = 1, nums = [0,1]
    # iter 4, fast = 3 (hit), slow = 1, nums = [0,1]
    # iter 5, fast = 4, slow = 2, nums = [0,1,3]
    # iter 6, fast = 5, slow = 3, nums = [0,1,3,0]
    # iter 7, fast = 6, slow = 4, nums = [0,1,3,0,4]
    # iter 8, fast = 7 (hit)
    # return len(nums[:slow])

    # [0,1,2,2,3,0,4,2]
    while fast < len(nums):
        if nums[fast] == val:
            pass
        else:
            nums[slow] = nums[fast] # [0], #[0,1], [0,1,3], ---> [0,1,3,0,4]
            slow += 1
        fast += 1
    return len(nums[:slow])

   


if __name__ == "__main__":

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(remove_element(nums, val))
