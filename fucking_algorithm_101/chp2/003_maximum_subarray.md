# Leetcode 53 - 最大子序列和

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

* 和最長遞增子序列套路相似

* brute force
  * 窮舉所有 element 對於 所有 1~element 加總 
  * tc : O(N^2)
  * sc : O(1)

* sliding window 
  * 初始 left, right 皆為 0
  * 擴大窗口 (合法解) - 加總 > 0
  * 縮小窗口 (優化答案) - 加總 < 0
  * 更新解答


```python
def sliding_window(nums : List[int]) -> int:
    '''
    nums = [-3,1,3,-1,2,-4,2]，算法返回 5，因为最大子数组 [1,3,-1,2] 的和为 5。
    pass
    '''
```


DP

1. 子問題、加總最大，可睇推至加上一個數字仍然最大

兩種定義 
* dp[i] : nums[0:i] 最大的子數組和 (連續的)
* dp[i] : 以 nums[i] 為最後的最大子數組和 (不用連續)

nums = [-3, `4`, `-1`, `2`, -6, 1, 4]
-->                      i

1. dp[i] = 4-1+2 = 5, dp[i+1] = 無法輕易和 dp[i] 扯上關係
2. dp[i] 以 nums[i] 為最後的組大子數組和 - 怎麼推廣到 dp[i+1]?
   1. 選擇和前面的數組連接，直接相加取最大, dp[i] = 5, dp[i+1] = 5
   2. 不與前面的數組連接，自己刑成子數組,

```python
dp[i] = max(nums[i], nums[i] + dp[i-1])
```


```python

def max_subarray(nums : List[int]) -> int:
    '''
    [-2,1,-3,4,-1,2,1,-5,4]
    [4,-1,2,1]
    return 6
    '''
    n = len(nums)
    if n == 0:
        return 0

    # dp [i] 紀錄以 nums[i] 為結尾的 最大子數組和
    dp = [0] * n
    # base case
    dp[0] = nums[0]
    # transition
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
        # [-2]
        # [-2, -1]
        # [-2, -1, -1] # 1 + (-3)
        # [-2, -1, -1, 3] 1 + (-3) + 4
        # [-2, -1, -1, 3, 5] 1 + (-3) + 4 + 2
        # [-2, -1, -1, 3, 5, 6] 1 + (-3) + 4 + 2 + 1
        # [-2, -1, -1, 3, 5, 6, 1]

    return max(dp)
    

```

# PreSum solution

# 總結

此題有三種聰明做法

1. sliding window
2. dp
3. presum