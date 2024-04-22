# 動態規劃解題套路框架

https://labuladong.online/algo/dynamic-programming/subsequence-problem/

子序列問題是常見的算法問題，而且不好解決

子序列 - 不用連續
子字串、子數組 - 必定連續

子序列 - 可能涉及兩個字串，例如最長公共子字串

--> 很難窮舉

**最長、最短子序列，幾乎可以肯定是考動態規劃，且時間複雜度是 $O(N^2)$**

--> 子序列的選擇通常時間複雜度是指數型成長，遇到指數型，先想動態規劃


# 兩種思路
## 1D dp array

```python
n = len(arr)
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        dp[i] = MinOrMax(dp[i], dp[j] + ...)
```

