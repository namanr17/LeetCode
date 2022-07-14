# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        index = {inorder[i]:i for i in range(n)}
        
        def build(i, start, end):
            if i == n:
                return None
            
            val = preorder[i]
            idx = index[val]
            
            node = TreeNode(val)
            
            if idx != start:
                node.left = build(i+1, start, idx-1)
            
            if idx != end:
                node.right = build(i+idx-start+1, idx+1, end)
                
            return node
        
        return build(0, 0, n-1)