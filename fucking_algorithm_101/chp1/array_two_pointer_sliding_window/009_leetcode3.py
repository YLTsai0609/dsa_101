'''

Medium

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''

from collections import defaultdict
from typing import List, Dict, Set

def brute_force(s : str, verbose : bool = True) -> str:
    '''
    算法流程
    '''
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            len(s[i:j]) == len(set(s[i:j])) # 建立 set 還要 O(N)
            # tc O(N^3)
            # hashtable 先建立， O(N^2)
            # window = defaultdict(int)


def sliding_window(s : str, verbose : bool = True) -> str:
    """
    "abcabcbb", 3
    bbbbb, 1
    pwwkew, 3
    tc : O(N_s)
    sc : O(N_s)
    """
    left, right = 0, 0
    window = defaultdict(int)
    curr_unq = 0

    # 右側窗口
    while right < len(s):
        c = s[right]
        right += 1

        # 窗口內資料更新
        window[c] += 1
        # Valid Solution
        
        if verbose:
            print(left, right, f'window : {window}, max_valid_char  : {curr_unq}')
        # 左側窗口，優化可行解，當字元數 > 1，說明有重複
        while window[c] > 1:
            d = s[left]
            left += 1

            # 窗口內資料更新
            window[d] -= 1
        curr_unq = max(curr_unq, right-left)
    
    return curr_unq


if __name__ == "__main__":
    questions = [
        ("abcabcbb", 3),
        ("bbbbbbbbb",1),
        ('pwwkew',3)
    ]
    
    verbose = True
    for func in [sliding_window]:
        for q in questions:
            s, ans = q
            pred = func(s=s, verbose=verbose)
            print(pred)
            # assert pred == ans
