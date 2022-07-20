# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if not node.left and not node.right:
                return node.val, 1, 1
            
            leftVal, leftCount, leftAns = solve(node.left) if node.left else (0, 0, 0)
            rightVal, rightCount, rightAns = solve(node.right) if node.right else (0, 0, 0)
            
            totalCount = leftCount + rightCount + 1
            totalVal = leftVal + rightVal + node.val
            totalAns = leftAns + rightAns
            
            if totalVal // totalCount == node.val:
                totalAns += 1
            
            return totalVal, totalCount, totalAns
        
        return solve(root)[2]