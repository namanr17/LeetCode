# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if not node.right and not node.left:
                return 0, node.val
            
            rightDepth, rightVal = solve(node.right) if node.right else (0, 0)
            leftDepth, leftVal = solve(node.left) if node.left else (0, 0)
            
            if leftDepth == rightDepth:
                return leftDepth + 1, leftVal + rightVal
            elif leftDepth > rightDepth:
                return leftDepth + 1, leftVal
            else:   return rightDepth + 1, rightVal
            
        return solve(root)[1]
                