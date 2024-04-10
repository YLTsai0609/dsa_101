'''
HARD

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

'''
brute_force

根據 t 建立 hashtable, {'A' : 1, 'B' : 1, 'C' : 1}
根據 s 兩次 loop
left, right, 展開子字串，並用 window 這個 hash table 紀錄出現的值
每個子字串，比對兩個 hashtable並記錄最新答案

tc : O(N_s^2)
sc : O(N_s) + O(N_t)
'''

'''
sliding window

s = "ADOBECODEBANC", t = "ABC", "BANC"

s = "a", t = "aa"

根據 t 建立 hashtable, {'A' : 1, 'B' : 1, 'C' : 1} need

left, right = 0, 0
need = defaultdict(int)
window = defaultdict(int)
valid_char = 0
min_cover = float('inf') # 一開始是無限大
min_cover_length = float('inf') # 一開始是無限大
for c in t:
    need[c] += 1

# 右側窗口
while right < len(s):
    c = s[right]
    right += 1
    
    # 更新窗口資料
    if c in need.keys():
        window[c] += 1
        if window[c] == need[c]:
            # 從 0 變成 1 時
            valid_char += 1
    
    # 左側窗口縮小條件為何? --> 所有字元都有了
    "ADOBECO" --> DOBECO
    while valid_char == len(need):
        # 更新答案
        if (right - left) < min_cover:
            min_cover_start = left
            min_cover_length = right - left
            min_cover = min(min_cover, s[min_cover_start : min_cover_start + min_cover_length])
        


        # 窗口縮減
        d = s[left]
        left +=1
        # 窗口資料更新
        if d in need.keys():
            if window[d] == need[d]:
            # 都是1時，才會減少
                valid_char -= 1
        window[d] -= 1
return '' if min_cover_length == float('inf')
        
    
'''