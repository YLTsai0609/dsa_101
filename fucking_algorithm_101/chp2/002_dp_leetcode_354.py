'''
longest increasing subsequence
hard
https://leetcode.com/problems/russian-doll-envelopes/

需要用 Binary Search, O(N^2) 會 TLE (Time Limit Exceeded)
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

def max_envelops(envelops : List[List[int]], verbose : bool = True) -> int:
    '''
    [[5,4],[6,4],[6,7],[2,3]] return 3
    題目說了 width 相同無法互套，所以 heights 降序排列，如果可以放，那麼 heights 也升序排列 (5,2) 可以放到 (5,4) 中
    '''
    envelops.sort(key=lambda x : (x[0], -x[1]))
    heights = [x[1] for x in envelops]
    if verbose:
        print(f'envelops : {envelops}', f'heights : {heights}')
    return length_of_lis(heights)


questions = [
    (
        [[5,4],[6,4],[6,7],[2,3]], 3
    )
]

for nums, res in questions:
    for _func in [
        max_envelops,
        ]:
        print(_func(nums))
