# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, left=True) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root, right=None) if left else TreeNode(val, left=None, right=root)
        
        if root.left:
            root.left = self.addOneRow(root.left, val, depth-1, True)
        elif depth == 2:
            root.left = TreeNode(val)
        
        if root.right:
            root.right = self.addOneRow(root.right, val, depth-1, False)
        elif depth == 2:
            root.right = TreeNode(val)
        
        return root
                