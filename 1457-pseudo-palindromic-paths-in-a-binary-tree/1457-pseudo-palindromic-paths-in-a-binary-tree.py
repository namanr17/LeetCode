# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = defaultdict(int)
        
        def dfs(node):
            freq[node.val] += 1
            
            flag, count_ = 0, 0
            if not node.left and not node.right:
                for k in freq:
                    count_ += freq[k] % 2
                    
                flag = 1 if count_ < 2 else 0
            
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
                
            freq[node.val] -= 1
            return left + right + flag
        
        return dfs(root)
            
            