"""
https://leetcode.com/problems/reverse-string/
easy
"""

from typing import List


def twopointer_sol(s: List[str]) -> List[str]:
    """
    tc : O(N/2)
    sc : O(1)
    """
    # 雙指標相向而行
    left = 0
    right = len(s) - 1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
        # 相等時元素不需調整
    return s


if __name__ == "__main__":
    s = ["H", "e", "l", "l", "o"]
    for func in [twopointer_sol]:
        print(func(s))
