# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solve(node: Optional[TreeNode]):
            if not node:
                return True, None, None
            
            leftFlag, leftMin, leftMax = solve(node.left)
            rightFlag, rightMin, rightMax = solve(node.right)
                
            if not leftFlag or not rightFlag:
                return False, None, None
            
            if node.left and node.val <= leftMax:
                return False, None, None
            
            if node.right and node.val >= rightMin:
                return False, None, None
            
            currMax = rightMax if node.right else node.val
            currMin = leftMin if node.left else node.val
            
            return True, currMin, currMax
        
        return solve(root)[0]