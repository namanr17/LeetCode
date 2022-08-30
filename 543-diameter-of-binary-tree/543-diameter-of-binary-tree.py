# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = -inf
        
        def getMaxGain(node):
            nonlocal maxLen
            
            left = getMaxGain(node.left) if node.left else 0
            right = getMaxGain(node.right) if node.right else 0
            
            maxLen = max(maxLen, 1 + left + right)
            
            return max(left, right) + 1
        
        getMaxGain(root)
        return maxLen - 1