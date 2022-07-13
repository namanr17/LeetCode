# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = Deque([])
        q.append(root)
        q.append('#')
        
        levelOrder = [[]]
        while(len(q)):
            node = q.popleft()
            if node == '#':
                if len(q):
                    levelOrder.append([])
                    q.append(node)
                    continue
                else:   break
                
            levelOrder[-1].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return levelOrder