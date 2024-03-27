'''

Hard 

consider string `s`, `t`, return sub-string `s` cover all `t` or None

* `t` 的重複字串，我們尋找的子字串字符數量，不應該小於 `t`
* `s` 如果存在 `t`, 必定是唯一解

e.g.

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。


输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？


'''

from collections import defaultdict
from typing import List, Dict, Set

def brute_force(s : str, t: str) -> str:
    '''
    tc : O(N^2)
    '''

def sliding_window(s : str, t : str, verbose : bool = True) -> str:
    """
    s = "ADOBECODEBANC", t = "ABC"
    return "BANC"
    tc : O(N)
    """
    # build hashtable for checking string t 
    need, window = defaultdict(int), defaultdict(int)
    for c in t:
        need[c] += 1

    # 左右指針 & 合法字元數
    left, right = 0, 0
    valid_chars = 0
    
    # 最小覆蓋字數和長度，需每次 iteration 更新
    min_cover_start, min_cover_length = 0, float('inf')

    while right < len(s):
        c = s[right]
        # 增大窗口
        right +=1
        # 進行窗口內資料的更新
        if c in need.keys():
            window[c] += 1
            if window[c] == need[c]:
                # 只有 window[c] 從 0 變成 1，才會合 need[c] 相等，進而讓 valid += 1，如果 window[c] 從1 , 變成 2 ，那麼不會符合
                valid_chars += 1 # valid 

        # debug 輸出位置，最終解法不要有 print，因為 IO 操作很耗時
        if verbose:
            print(left, right, f'window : {s[left:right]}')

        # 判斷左側窗口要不要收縮，優化合法解
        while valid_chars == len(need):
            # 更新答案的規則
            if (right - left) < min_cover_length:
                min_cover_start = left
                min_cover_length = right - left
            
            # 縮減窗口
            d = s[left]
            left += 1
            # 進行窗口內資料更新
            if d in need.keys():
                if window[d] == need[d]:
                    # 只有接等於 1 時， 合法字元數變少，其他情況，則是 window 內的關鍵字次數少一次
                    valid_chars -= 1
                window[d] -= 1
    

    return '' if min_cover_length == float('inf') else s[min_cover_start : min_cover_start + min_cover_length]



if __name__ == "__main__":
    questions = [
        ('ADOBECODEBANC','ABC','BANC')
    ]
    
    verbose = True
    for func in [sliding_window]:
        for q in questions:
            s, t, ans = q
            pred = func(s=s, t=t, verbose=verbose)
            assert pred == ans
