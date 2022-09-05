"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    return []
        
        dq, ret = deque([root]), []
        
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                for child in node.children:
                    dq.append(child)
            ret.append(level)
        
        return ret