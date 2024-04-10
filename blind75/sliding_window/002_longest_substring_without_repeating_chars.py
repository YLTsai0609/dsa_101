'''
Given a string s, find the length of the longest substring
 without repeating characters.

Examples
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
brute force
兩次 loop, 每次 i, j 取出substring
1. 每次都建立 set ，比較數量是否一致
    tc : O(N^3)
    sc : O(N)

    用一個 hashtable 做 window， 一但 window[c] 有等於 2 停止，記錄答案
    tc : O(N^2)
    sc : O(N)
'''

'''
"abcabcbb" --> abc
sliding window
left, right = 0, 0
window = defaultdict(int)
curr_unq = 0

while right < len(s):
    # 右側窗口
    c = s[right]
    right += 1
    
    # 更新窗口資料
    window[c] += 1

    # verbose print 窗口資料
    
    # 左側窗口，優化合法解
    # abca, 出現重複值，要被優化
    while window[c] > 1:
        d = s[left]
        left += 1

        # 更新窗口資料
        window[d] -= 1
    
    # 更新答案
    curr_unq = max(curr_unq,right-left)

tc : O(N)
sc : O(1)
'''