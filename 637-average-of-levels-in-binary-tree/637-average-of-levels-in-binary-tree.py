# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = defaultdict(float)
        count = defaultdict(float)
        
        def dfs(node, h=0):
            if not node:    return h
            
            level[h] += node.val
            count[h] += 1
            
            return max(dfs(node.left, h+1), dfs(node.right, h+1))
            
        ret = [0] * dfs(root)
        
        for h in level:
            ret[h] = level[h] / count[h]
        
        return ret