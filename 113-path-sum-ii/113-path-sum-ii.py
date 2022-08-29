# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:    return []
        q, ret = deque(), []
        
        def dfs(node, sum_):
            q.append(node.val)
            sum_ += node.val
            
            if not node.left and not node.right and sum_ == targetSum:
                ret.append(list(q))
            
            if node.left:
                dfs(node.left, sum_)
            if node.right:
                dfs(node.right, sum_)
            
            q.pop()
            
        dfs(root, 0)
        return ret