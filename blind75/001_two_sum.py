"""
leetcode 1

nums = [2,7,11,5]
target = 9

Output = [0,1]
"""

"""
for i in range(len(nums)):
    for j in range(len(unms)):
    # tc : O(N^2)
    # sc : O(1)
"""

"""
build hashtable
for i in range(len(nums)):
    target - nums[i] in hashtable
    # tc : O(N)
    # sc : O(N)
"""

""" TwoSum2
if array element is sorted
two pointers
    # tc : O(N)
    # sc : O(1)

    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left] + nums[right] == target:
            return [left, right]
        nums[left] + nums[right] > target: 
            # 如果排序好了，只有可能是需要一個更小的值
            right -= 1
        nums[left] + nums[right] < target:  
            # 如果排序好了，只有可能是需要一個更大的值
            left += 1
"""