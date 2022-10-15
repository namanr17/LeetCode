# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        
        def solve(node, parenVal):
            if node.val != parenVal:
                solve(node, node.val)
                return 0
            
            left = solve(node.left, node.val) if node.left else 0
            right = solve(node.right, node.val) if node.right else 0
            
            nonlocal ans
            ans = max(ans, left + right + 1)
            return max(left, right) + 1
        
        solve(root, root.val)
        return ans - 1