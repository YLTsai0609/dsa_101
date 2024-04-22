'''
longest increasing subsequence
medium
https://leetcode.com/problems/longest-increasing-subsequence/description/
'''



from typing import List

def brute_force():
    pass

def length_of_lis(nums : List[int], verbose : bool = True) -> int:
    '''
    nums=[1,4,3,4]
    dp = [1,2,2,3]
    return 3
    '''
    # dp[n]，以第n個 element 為結尾的最長遞增序列數量
    dp = [1] * len(nums) # 每個 elements 的 base case 都是 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                # nums[i] 可以成為 子序列遞增的一部分，相等時不要成為子浚洌
                dp[i] = max(dp[i], dp[j] + 1) # tc : O(1)
    if verbose:
        print(dp)
    return max(dp)



questions = [
    ([1,4,3,4], 3),
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1)
]

for nums, res in questions:
    for _func in [
        length_of_lis,
        ]:
        print(_func(nums, res))
