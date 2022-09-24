"""
https://leetcode.com/problems/longest-palindromic-substring/
medium
"""

from typing import List


def is_palindrome(s: str) -> str:
    """
    tc : O(N)
    sc : O(1)
    """
    left = 0
    right = len(s) - 1
    while left < right:
        print(s[left], s[right])
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def substring_palindrome(s: str, left: int, right: int) -> str:
    """
    """
    # 雙指標背向而行
    # 相同 left, right, s=4,

    # 不掉出邊界
    while (left >= 0 and right < len(s)) and (s[left] == s[right]):
        # 以 left, right 為中心向外擴展
        # left == right : 奇數
        # left right 相鄰 : 偶數
        left -= 1
        right += 1
    return s[left + 1 : right]


def longest_palindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        s_odd = substring_palindrome(s, i, i)
        s_even = substring_palindrome(s, i, i + 1)
        if len(s_odd) > len(res):
            res = s_odd
        if len(s_even) > len(res):
            res = s_even
    return res


if __name__ == "__main__":
    s1 = "babad"
    s2 = "cbbd"
    s3 = "aba"
    s4 = "asdfgfdsa"
    for s in [s1, s2, s3, s4]:
        # print(s)
        # print(is_palindrome(s))
        print(longest_palindrome(s))
    # print(substring_palindrome(s1, 2, 2))
    # print(substring_palindrome(s4, 4, 4))
