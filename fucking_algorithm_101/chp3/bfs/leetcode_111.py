# Definition for a binary tree node.
# https://leetcode.com/problems/minimum-depth-of-binary-tree/?source=submission-noac

from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        visited = set()
        if root:
            q.append(root)
            visited.add(root)
        else:
            return 0

        depth = 1 # root = level 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft() # tree-node
                # root
                # match the mim level
                if cur:
                    if not cur.left and not cur.right:
                        return depth
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            depth += 1
        return depth
        
#TODO
# how to build test case?