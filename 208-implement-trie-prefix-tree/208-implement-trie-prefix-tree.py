class Trie:
    class Node:
        """A node in the trie"""
        
        def __init__(self, char='\0', parent=None):
            self.children = {}
            self.char = char
            self.final = False
            self.parent = parent
            
        def descend(self, char, extend=False):
            """Descend into the trie"""
            
            if not char in self.children:
                if not extend: return None
                self.children[char] = Trie.Node(char,self)
                
            return self.children[char]

    def __init__(self):
        self.root = Trie.Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            node = node.descend(char, extend=True)
        node.final = True

        
    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            node = node.descend(char, extend=False)
            if not node:    return False
        
        return node.final

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            node = node.descend(char, extend=False)
            if not node:    return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)