# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        maxWidth = 0
        
        while(q):
            n = len(q)
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)
            
            while(n):
                node, idx = q.popleft()
                if node.left:   q.append((node.left, idx*2))
                if node.right:  q.append((node.right, idx*2 + 1))
                n -= 1
        
        return maxWidth
        