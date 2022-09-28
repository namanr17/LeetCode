class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.toDelete = False

    def addPath(self, path):
        node = self
        for p in path:
            node = node.children[p]
                    
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def hashFolderPaths(node):
            if not node.children:   return ''
            
            keys = [c + '/' + hashFolderPaths(child) for c, child in node.children.items()]
            key =  '(' + ''.join(keys) + ')'
            
            seen[key].append(node)
            return key
        
        
        def dfsPaths(node, path):
            for c, child in node.children.items():
                if not child.toDelete:
                    ans.append(path + [c])
                    dfsPaths(child, path + [c])
            
        
        trie = TrieNode()
        for path in sorted(paths):
            trie.addPath(path)
            
        seen = defaultdict(list)
        hashFolderPaths(trie)
        
        # for n in seen:
        #     print(n, len(seen[n]))
        
        for nodes in seen.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.toDelete = True
        
        ans = []
        dfsPaths(trie, [])
        return ans
        