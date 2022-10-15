class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = 0
        def traverse(node):
            if not node:    return 0
            nonlocal longest
            
            left_len, right_len = traverse(node.left), traverse(node.right)
            
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            
            longest = max(longest, left + right)
            return max(left, right)
        
        traverse(root)
        return longest