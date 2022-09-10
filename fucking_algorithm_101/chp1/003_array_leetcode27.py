"""
https://leetcode.com/problems/remove-element/solution/
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
    while fast < len(nums):
        if nums[fast] == val:
            pass
        else:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    # return nums[:slow]
    return len(nums[:slow])


if __name__ == "__main__":

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(remove_element(nums, val))
