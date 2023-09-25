from pyparsing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root.val is None: return False
        if targetSum - root.val == 0: return True
        if targetSum - root.val < 0: return False
        return self.hasPathSum(root.left, targetSum - root.val) or \
         self.hasPathSum(root.right, targetSum - root.val)
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,s):
            if not node:
                return
            s += (node.val)
            if node.left is None and node.right is None:
                if s == targetSum:
                    return True
            return dfs(node.left,s) or dfs(node.right,s)
        return dfs(root,0)


A = Solution()
