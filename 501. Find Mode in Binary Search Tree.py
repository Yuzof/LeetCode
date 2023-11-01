# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        self.inorderr = []
        def inorder(root):
            if not root: return
            self.inorderr.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)        
        freq = collections.Counter(self.inorderr)
        maxx = max(freq.values())
        return [x for x in freq if freq[x] == maxx]