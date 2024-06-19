'''
https://labuladong.online/algo/practice-in-action/nsum/#%E4%B8%89%E3%80%814sum-%E9%97%AE%E9%A2%98

1. leetcode 1 two-sum without the same elements
2. leetcode 167 two-sum II with sorted elements
3. modified two-sum , result is not nuique
([1,3,1,2,2,3],4, [[1,3], [2,2]]), note: cannot return [[1,3],[1,3],[2,2]]
4. Leetcode 15 - 3Sum - i!=j, i!=k, j!=k return dististinct triplets
5. Leetcode 18 - 4Sum
'''
from typing import List

def two_sum_hash(nums : List[int], target : int) -> List[int]:
    '''
    hash table 
    tc : O(N)
    sc : O(N)

    two-pointer
    1. need to sort the array first
    2. apply two-pointer
    '''
    values_with_index = {}
    # res = []
    for idx, ele in enumerate(nums):
        values_with_index[ele] = idx
    for ele in nums:
        # Search on O(1)
        if target - ele in values_with_index.keys():
            return [ele, target-ele]


def two_sum_two_pointer(nums : List[int], target : int) -> List[int]:
    '''
    tc : O(nlogn) + O(n) = O(nlogn)
    sc : O(1)
    '''
    # sort - if quick sort - O(NlogN)
    nums.sort()
    # apply left, right two-pointer
    left = 0
    right = len(nums) - 1
    # 交叉時搜尋完畢
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum < target:
            # left 要變大
            left += 1
        elif curr_sum > target:
            # right 要變小
            right -=1
        elif curr_sum == target:
            return [nums[left], nums[right]]

def two_sum_two_pointer_with_multiple(nums : List[int], target : int) -> List[int]:
    '''
    tc : O(nlogn) + O(n) = O(nlogn)
    sc : O(1)
    (
        [1,3,1,2,2,3],
        4,
        [[1,3], [2,2]]
    )
    '''
    # sort - if quick sort - O(NlogN)
    nums.sort()
    # apply left, right two-pointer
    left = 0
    right = len(nums) - 1
    res = []
    # 交叉時搜尋完畢
    while left < right:
        # [1,1,2,2,3,3]
        low = nums[left] # 1
        high = nums[right] # 3
        curr_sum = low + high # 4 nums[3] + nums[4] = 4
        if curr_sum < target:
            # left 要變大
            left += 1
        elif curr_sum > target:
            # right 要變小
            right -=1
        elif curr_sum == target:
            # [1,3,1,2,2,3] --> [1,1,1,2,2,3,3]
            # [ [1,3],[2,2] ]
            res.append([low, high])
            # skip all the duplicates
            while nums[left] == low:
                left += 1 # left = 2, nums[2] == 1, left=3
            while nums[right] == high:
                right -= 1
                # right = 4
    return res

def sorted_two_sum_two_pointer_left(
        nums : List,
        target : int,
        left : int = 0,
        need_sorted : bool = True) -> List[int]:
    '''
    [1,3,1,2,2,3],4, [[1,3], [2,2]]
    '''
    if need_sorted:
        nums.sort() # [1,1,2,2,3]
    # 不做 sort，外面做過了
    right = len(nums) - 1
    res = []
    # 交叉時停止
    while left < right:
        low = nums[left] 
        high = nums[right]
        curr_sum = low + high
        if curr_sum < target:
            # 加總太小，需要變大
            left += 1
        elif curr_sum > target:
            # 加總太大，需要變小
            right -= 1
        elif curr_sum == target:
            res.append([low, high])
            # 略過重複值
            while left < right and nums[left] == low:
                left += 1
            while left < right and nums[right] == high:
                right -= 1
    return res

def three_sum_two_pointer(nums : List[int], target : int) -> List[int]:
    '''
    for loop the elements
    target - nums, then the problem becomes two-sum
    (
        [-1,0,1,2,-1,-4], 0,
        [[-1,-1,2],[-1,0,1]]
    ),

    ([0,1,1], 0, []),
    ([0,0,0], 0, [[0,0,0]])
    tc : 
        sort : O(nlogn) quick sort / merge sort
        loop over each elements + two-pointer
            O(N^2)
    sc : 
        O(1)
    tc : O(N^2)
    '''
    # in-order-to solve by two-pointer
    nums.sort() # [-4, -1, -1, 0, 1 , 2]
    n = len(nums)
    res = []
    i = 0
    while i < n-1:
        # -4, twoSum with nums, target = 4, got [] (no answer)
        # -1, twoSum with nums, target = 1, got [[-1, 2], [0,1]]
        # 需要 skip 下一個 -1, i = 1, num[1] = -1, nums[2] = -1
        curr_ele = nums[i] 
        # -1
        # 1, 
        # [[0,1], [-1,2]]
        tuples : List[List[int]] = sorted_two_sum_two_pointer_left(
            nums, 
            target=target - curr_ele,
            left=i+1,
            need_sorted=False
            )
        if tuples:
            for t in tuples:
                res.append([curr_ele, *t])
        # skip the duplicates
        while i < n-1 and nums[i] == curr_ele:
            i += 1
    return res


if __name__ == "__main__":
    # two_sum_questions = [
    #     ([1,3,5,6], 9, [3,6]),
    # ]
    # for nums, target, ans in two_sum_questions:
    #     for func in [two_sum_hash, two_sum_two_pointer]:
    #         print(func(nums, target))

    # two_sum_duplicates_questions = [
    #     ([1,3,1,2,2,3],4, [[1,3], [2,2]])
    # ]
    # for nums, target, ans in two_sum_duplicates_questions:
    #     for func in [two_sum_two_pointer_with_multiple, sorted_two_sum_two_pointer_left]:
    #         print(func(nums, target))

    three_sum_questions = [
        ([-1,0,1,2,-1,-4], 0, [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], 0, []),
        ([0,0,0], 0, [[0,0,0]])
    ]
    for nums, target, ans in three_sum_questions:
        for func in [three_sum_two_pointer]:
            print(func(nums, target))



# https://www.1point3acres.com/bbs/thread-1021536-1-1.html