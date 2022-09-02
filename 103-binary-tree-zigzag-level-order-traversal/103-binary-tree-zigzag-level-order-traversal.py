# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        
        dq = deque([root])
        ret = []
        
        while(dq):
            level, tmp = [], deque()
            
            while(dq):
                node = dq.popleft()
                level.append(node.val)
                if node.left:   tmp.append(node.left)
                if node.right:  tmp.append(node.right)
            
            if len(ret) % 2:
                ret.append(level[::-1])
            else:   ret.append(level[:])
                
            dq = tmp
        
        return ret
                
            