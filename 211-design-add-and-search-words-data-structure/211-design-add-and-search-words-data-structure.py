class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word: str) -> bool:

        def dfs(idx, node) -> bool:
            if idx == len(word):
                return '#' in node
            
            if word[idx] == '.':
                for child in node:
                    if child != '#' and dfs(idx+1, node[child]):
                        return True
                    
            if word[idx] in node:
                return dfs(idx+1, node[word[idx]])
            
            return False
        
        return dfs(0, self.trie)