# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(lo, hi):
            if lo > hi:
                return None

            mid = (lo + hi) // 2
            leftNode, rightNode = None, None
            
            if lo < mid:
                leftNode = build(lo, mid-1)
            if mid < hi:
                rightNode = build(mid+1, hi)
        
            return TreeNode(nums[mid], leftNode, rightNode)
        
        return build(0, len(nums)-1)