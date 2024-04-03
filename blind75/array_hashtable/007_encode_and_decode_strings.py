"""
leetcode 347
Medium


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



"""

from typing import List
from collections import defaultdict

def brute_force(nums: List[int], k : int) -> List[int]:
    # build hash table
    # tc : O(N)
    # sc : O(N)
    counts = {}
    for e in nums:
        counts[e] += 1
    
    # sort-hashtable by values
    # O(n log n )
    # 泡泡 O(N^2)
    # quick sort, merge sort O(n log n)
        

def freq_table_with_bucket(nums: List[int], k : int, verbose : bool = True) -> List[int]:
    '''
    [1,1,1,2,2,3]
    '''
    res = []
    # 建立頻率表
    num_freq = defaultdict(int)
    for e in nums:
        num_freq[e] += 1
    # {1 : 3, 2 : 2, 3 : 1}
    # 頻率表絕對是正的，而且 key 會從 0 ~ N，最多出現 N 次，最少出現 0 次
    # 建立 buckets, index 指的是出現次數，從 0 ~ N
    #  0   , 1, 2, 3, 4,  ,    5,   6
    # [None, 3, 2, 1, None, None, None]
    buckets = [None for _ in range(len(nums))]

    for num, freq in num_freq.items():
        buckets[freq] = num
    
    if verbose:
        print(num_freq,buckets, sep='\n')
    # 從 buckets 最後一個元素跑回來，取 topk
    
    for i in range(len(nums), 0, -1):
        num = buckets[i - 1]
        print(i, num)
        if num:
            res.append(num)
    return res[:k]
    


# def bucket_sort(nums: List[int], k : int, verbose : bool = True) -> List[int]:
# 如果有複數，就死了
#     # 借鑑 count sort (index-based sort)
#     # nums 有多大， 就建立一個 nums 的 array，每一個 element 都是一個 array
    
#     # for loop nums，根據元素放進 buckets 的 index，用 append
    
#     # for loop buckets，一路排出來，就排序完了

#     # sc O(2N) : N is the length of nums
#     # tc O(2N) : build table and sort in buckets

#     res = []

#     bucket = [
#         [] for _ in range(len(nums))
#     ]
    
#     # index-based 
#     for e in nums:
#         bucket[e].append(e)
#     if verbose:
#         print(bucket)
#     for idx, bk in enumerate(bucket):
#         if len(bk) > 0:
#             _got = bk.pop()
#             res.append(_got)
#     return res[:k]


questions = [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([-1,-1,-1,2,2,3], 2, [-1,2])
]



validate = True
for q in questions:
    nums, k, sol = q
    for func in [freq_table_with_bucket]:
        pred = func(nums, k)
        print(pred)
        if validate:
            assert sol == pred
        


'''
bucket sort 要借助頻率表，才能將 nums mapping 1~N
''' 
    
