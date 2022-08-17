# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'None'
        
        data = []
        q = deque([root])
        while(q):
            k = len(q)
            while(k):
                k -= 1
                node = q.popleft()
                if not node:
                    data.append('None')
                    continue
                
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ' '.join(data)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        leveledTree = data.split(' ')
        
        if leveledTree[0] == 'None':
            return None
        
        itr = 1
        root = TreeNode(leveledTree[0])
        q = deque([root])
        while(q):
            k = len(q)
            while(k):
                node = q.popleft()
                left, right = leveledTree[itr], leveledTree[itr+1]
                
                if left != 'None':
                    node.left = TreeNode(int(left))
                    q.append(node.left)
                
                if right != 'None':
                    node.right = TreeNode(int(right))
                    q.append(node.right)
                
                k -= 1
                itr += 2
        
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans