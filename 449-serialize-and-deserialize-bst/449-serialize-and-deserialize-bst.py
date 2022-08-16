class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        
    def deserialize(self, data: str) -> TreeNode:
        deq = deque(int(val) for val in data.split(',') if val)
        
        def build_tree(lower_bound, upper_bound):
            if deq and lower_bound < deq[0] < upper_bound:
                val = deq.popleft()
                return TreeNode(val, build_tree(lower_bound, val), build_tree(val, upper_bound))
               
        return build_tree(float('-inf'), float('inf'))