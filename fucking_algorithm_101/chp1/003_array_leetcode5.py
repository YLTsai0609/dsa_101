"""
https://leetcode.com/problems/longest-palindromic-substring/
medium

other sol

https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome#approach-2-brute-force

babad

brute force : 
1. 展開所有 substring : O(N^2), including trivial solution (single word)
	- b, ba, bab, baba, babad
	- a, ba, ab, aba, abad,
	- ...
2. verify palindrome : O(N) for each substring
tc : O(N^3)
sc : O(1)

dynamic programming v1:

improved version of brute force
	- 很多 sub string 不用重算
	- bab 是回文
	- ababa 一定是回文，只要比最外面左跟右一樣就行了，不用全比
	- P(left, right) 是不是回文(left, right is index of array) : 
		- Sleft, Sright 是回文, true
		- otherwise, false
	- P(left, right) = (P(left+1, right-1) and Sleft == Sright), i是左, j是右
	- base cases : P(left, left) = True, P(left, left+1) == (s[left] == s[left+1]), build lookup table
	- create lookup table sc : O(N^2)
	- tc : O(N^2)

dynamic programming v2:
	- v1 優化版 P(left, right) = (P(left + 1, right-1) and Sleft == Sright) 只 depends on 上一層，不用存整個 matrix
    - sc : O(N)
    - tc : O(N^2)


Manacher's Algorithm
tc : O(N)
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """
    tc : O(N)
    sc : O(1)
    """
    left = 0
    right = len(s) - 1
    while left < right:
        # print(s[left], s[right])
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def brute_force(s: str) -> str:
    """
    tc : O(N^2)
    sc : O(1)
    debug this
    """
    res = ""
    for left in range(len(s)):
        for right in range(len(s)):
            if is_palindrome(s[left : right + 1]):
                curr_substring = s[left : right + 1]
                res = curr_substring if len(curr_substring) > len(res) else res
    return res


def substring_palindrome(s: str, left: int, right: int) -> str:
    """
    tc : O(N)
    sc : O(1)
    """
    # 雙指標背向而行
    # 相同 left, right, s=4, abba

    # 不掉出邊界
    while (left >= 0 and right < len(s)) and (s[left] == s[right]):
        # 以 left, right 為中心向外擴展
        # left == right : 奇數
        # left right 相鄰 : 偶數
        left -= 1
        right += 1
    return s[left + 1 : right]


def twopointer(s: str) -> str:
    """
    tc : O(N)
    sc : O(k) --> longest palindrome
    """
    res = ""
    for i in range(len(s)):
        s_odd = substring_palindrome(s, i, i)
        s_even = substring_palindrome(s, i, i + 1)
        if len(s_odd) > len(res):
            res = s_odd
        if len(s_even) > len(res):
            res = s_even
    return res


def dp(s: str) -> str:
    """
    babad
    tc : O(N^2)
    sc : O(N^2)
    """
    if s == "":
        return s

    res = ""
    # look up table for fast check 回文	(len(s) x len(s)) matrix
    lookup = [[None for i in range(len(s))] for j in range(len(s))]

    for right in range(len(s)):
        for left in range(right, -1, -1):
            # print(right, left)
            # we need to make sure
            # lookup[left+1][right -1] is ready for lookup[left][right]
            # 0, 0
            # 1, 1
            # 1, 0
            # 2, 2
            # 2, 1
            # 2, 0
            # base case
            if left == right:
                lookup[left][right] = True
            # base case
            elif right == left + 1:
                lookup[left][right] = s[left] == s[right]
            else:
                lookup[left][right] = (lookup[left + 1][right - 1]) and (
                    s[left] == s[right]
                )  # 一路往外比即可，不用比 substring

            # update 最長回文字串
            curr_substring = s[left : right + 1]
            if (lookup[left][right]) and (len(curr_substring) > len(res)):
                res = curr_substring
    return res


def dp_v2(s: str) -> str:
    if s == "":
        return s
    res = ""
    lookup = [None for i in range(len(s))]
    for right in range(len(s)):
        for left in range(right + 1):
            # update lookup at level = right, using dp table at level = right - 1
            if left == right:
                lookup[left] = True
            elif right == left + 1:
                lookup[left] = s[left] == s[right]
            else:
                lookup[left] = lookup[left + 1] and (s[left] == s[right])

            curr_substring = s[left : right + 1]
            if lookup[left] and len(curr_substring) > len(res):
                res = curr_substring
    return res


def manacher_algo(s: str) -> str:
    """
    https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
    """
    pass


if __name__ == "__main__":
    s1 = "babad"
    s2 = "cbbd"
    s3 = "aba"
    s4 = "asdfgfdsa"
    for s in [s1, s2, s3, s4]:
        # print(s)
        # print(is_palindrome(s))
        print(f"input : {s}")
        for func in [brute_force, twopointer, dp, dp_v2]:
            print(f"{func.__name__} : ", func(s))
    # print(substring_palindrome(s1, 2, 2))
    # print(substring_palindrome(s4, 4, 4))
