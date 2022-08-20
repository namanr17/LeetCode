# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = None
        
        def findLCA(node):
            nonlocal lca
            if not node:
                return False
            
            if node.val in {startValue, destValue}:
                lca = node
                return True
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            if left and right:
                lca = node
                return True
            
            return left or right
        
        findLCA(root)
        path = []
        
        def findStart(node):
            if node.val == startValue:
                return True
            
            # nonlocal path
            if node.left and findStart(node.left):
                path.append('U')
                return True
            
            if node.right and findStart(node.right):
                path.append('U')
                return True
            
            return False
            
        def findDest(node):
            if node.val == destValue:
                return True
            
            nonlocal path
            if node.left and findDest(node.left):
                path += 'L'
                return True
            
            if node.right and findDest(node.right):
                path += 'R'
                return True
            
            return False
        
        findDest(lca)
        findStart(lca)
        
        return ''.join(path[::-1])
        