"""
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

1 <= s.length, t.length <= 5*10^4
s and t consist of lowercase English letters.

* 討論點
    * 有沒有大小寫的分別
    * 字串會多長?

* 是否為字謎
    * 長度相同
    * 相同字元個數相同
"""

'''
brute force

for c1 in range(s1):
    O(N^2), remove 的話 O(3)
    if c1 in s2:
        remove 
'''

'''
hash table h1
build s1 as hashtable with counting
for c2 in range(s2):
    if c2 in h1
        h1[c2] -= 1
return sum(h1.values) == 0

tc : O(N)
sc : O(1) 最多 26 個字母， key 最多 26 個
'''