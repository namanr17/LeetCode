# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        ret = defaultdict(list)
        
        def solve(root, h=0):
            ret[h].append(root.val)
            if root.left:
                solve(root.left, h+1)
            if root.right:
                solve(root.right, h+1)
        
            return
        
        solve(root, 0)
        
        return [ret[i] for i in list(ret.keys())[::-1]]