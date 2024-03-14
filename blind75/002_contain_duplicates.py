"""
nums = [1,2,3,1]
True

nums = [1,2,3,2]
True

[1,2,3,4]
False


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

"""
雙指標可以解嗎?

除非 element 排序好，不然不行，意思就是說，要先排序

tc : O(nlogn) + O(n)
sc : O(1) <-- depends on your sorting algorithm

但如果使用 hashtable，可以 O(n)
"""