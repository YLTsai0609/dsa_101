'''

Medium

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
'''

from collections import defaultdict
from typing import List, Dict, Set

def brute_force(s : str, p: str, verbose : bool = True) -> str:
    '''
    算法流程
    1. p string - 建立一個 hashtable, 並儲存長度 len_p
    2. for i in range(len(s)):
        s[i : i + len_p] 比對是否相等
        if 相等:
            res.append(i)
    
    tc : O(N_s)
    sc : O(N_p)
    # 這一題，固定窗口也可以解
    # 如果每一次要比對字串 p，那麼則是 tc O(N_s * N_p)
    '''

    need = defaultdict(int)
    for c in p:
        need[c] += 1
    
    left = 0
    res = []
    # 等同於 for loop, len(need) = 3
    while left + len(need) <= len(s):
        if set(s[left : left + len(need)]) == set(need.keys()): # 不管順序，完全吻合
            res.append(left)
        left += 1
        print(s[left : left + len(need)])
    return res


def sliding_window(s : str, p : str, verbose : bool = True) -> str:
    """
    "cbaebabacd", "abc", [0,6]
    tc : O(N_s)
    sc : O(n_p)
    """
    window, need = defaultdict(int), defaultdict(int)
    # build hashtable for checking permutation
    for c in p:
        need[c] += 1
    left, right, valid_char = 0, 0, 0
    res = []
    
    # 右側窗口，獲得合法解
    while right < len(s):
        c = s[right]
        # 增大窗口
        right += 1
        # 窗口內的資料更新
        if c in need.keys():
            window[c] += 1
            # 獲得合法解，必定從 0 -> 1 才有
            if window[c] == need[c]:
               valid_char += 1 

        # debug
        if verbose:
            print(left, right, f'window : {s[left : right]}', valid_char)

        #左側窗口是否要縮小，優化合法解
        while right - left >= len(p):
            if valid_char == len(need):
                res.append(left)
            
            # 縮減窗口
            d = s[left]
            left += 1

            # 窗口內資料更新
            if d in need.keys():
                if window[d] == need[d]:
                    valid_char -= 1
                window[d] -= 1
            
            # NOTE: 因為其實是固定大小的掃描，所以先更新資料，在縮減窗口
    return res


if __name__ == "__main__":
    questions = [
        ("cbaebabacd", "abc", [0,6]),
        ("abab",'ab', [0,1,2])
    ]
    
    verbose = True
    for func in [brute_force, sliding_window]:
        for q in questions:
            s, p, ans = q
            pred = func(s=s, p=p, verbose=verbose)
            assert pred == ans
