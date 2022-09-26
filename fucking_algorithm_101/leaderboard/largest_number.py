"""
# 179
https://leetcode.com/problems/largest-number/

sort algorithm : O(nlogn)
such as 
    merge sort, quick sort : O(NlogN)
    bubble sort : O(N^2)

"""

from typing import List


class compare(str):
    def __lt__(x, y):
        return x + y > y + x


def compare_by_concat(nums: List[int]) -> str:
    sorted_nums = sorted([str(x) for x in nums], key=compare)
    if sorted_nums[0] == "0":
        return 0
    else:
        return "".join(sorted_nums)


def compare_by_factor(nums: List[int]) -> str:
    """
    轉字串解
    """
    nums = [str(x) for x in nums]
    # 需要知道最大長度
    maxL = max([len(x) for x in nums])
    # factor = (maxL // len(x) + 1)
    nums.sort(key=lambda x: x * (maxL // len(x) + 1), reverse=True)
    # print(nums, maxL, [x * (maxL // len(x) + 1) for x in nums])
    if nums and nums[0] == "0":
        return "0"
    return "".join(nums)


if __name__ == "__main__":
    nums1 = [10, 2]
    nums2 = [
        3,
        30,
        34,
        5,
        9,
    ]  # expected ans : "9 5 34 3 30", cannot break the ans : 9 5 43 3 30
    nums3 = [42, 420]
    nums4 = [42, 422]
    nums5 = [0, 42]
    nums6 = [0, 0]
    for nums in [nums1, nums2, nums3, nums4, nums5, nums6]:
        print("input : ", nums)
        for func in [compare_by_concat, compare_by_factor]:
            print(f"{func.__name__} : ", func(nums))
