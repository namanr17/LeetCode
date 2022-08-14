class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        charList = [char for char in string.ascii_lowercase]
        
        if endWord not in wordList:
            return 0
        
        nodes = set(wordList + [beginWord])
        queue = deque([beginWord])
        ret = 0
        
        while(queue):
            ret += 1
            
            workingSet = set(queue.copy())
            queue.clear()
            
            for word in workingSet:
                nodes.remove(word)
                if word == endWord:
                    return ret
                for i in range(len(word)):
                    for char in charList:
                        destWord = word[:i] + char + word[i+1:]
                        if destWord in nodes and destWord not in workingSet:
                            queue.append(destWord)
                            
        return 0