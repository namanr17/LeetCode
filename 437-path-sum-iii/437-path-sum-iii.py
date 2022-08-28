# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:    return 0
        
        numPaths = Counter([0])
        count = 0
        
        def dfs(node, runSum):
            nonlocal targetSum, count
            runSum += node.val
            
            count += numPaths[runSum - targetSum]
            numPaths[runSum] += 1
            
            if node.left:   dfs(node.left, runSum)
            if node.right:  dfs(node.right, runSum)
                
            numPaths[runSum] -= 1
        
        dfs(root, 0)
        return count
            
            