# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        
        dq, levelOrder = Deque([root]), []
        
        while(dq):
            n, level = len(dq), []

            for _ in range(n):
                node = dq.popleft()
                level.append(node.val)
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
                
            levelOrder.append(level)
        
        return levelOrder