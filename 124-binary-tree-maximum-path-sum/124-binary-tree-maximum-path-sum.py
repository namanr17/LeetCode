# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -inf
        
        def getMaxGain(node):
            nonlocal maxSum
            
            leftGain = max(getMaxGain(node.left), 0) if node.left else 0
            rightGain = max(getMaxGain(node.right), 0) if node.right else 0
            
            maxSum = max(maxSum, node.val + leftGain + rightGain)
            
            return max(leftGain, rightGain) + node.val
        
        getMaxGain(root)
        return maxSum