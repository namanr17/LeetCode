# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        dq = deque([root])
        
        while(dq):
            n = len(dq)
            ret.append(0)
            
            for _ in range(n):
                node = dq.popleft()
                ret[-1] += node.val
                
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            
            ret[-1] /= n
        
        return ret
        