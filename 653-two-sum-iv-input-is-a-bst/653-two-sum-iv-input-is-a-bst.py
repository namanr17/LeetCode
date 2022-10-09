# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.toFind = {None}
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:    return False
        
        if root.val in self.toFind:
            return True
        
        self.toFind.add( k - root.val )
        
        return self.findTarget( root.left, k ) or self.findTarget( root.right, k )
        