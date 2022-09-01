# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, mx = -inf) -> int:        
        if not root:    return 0
        mx = max(mx, root.val)
        return (root.val >= mx) + self.goodNodes(root.left, mx) + self.goodNodes(root.right, mx)