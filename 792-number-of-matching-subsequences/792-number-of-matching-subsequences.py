class Node:
    def __init__(self, word):
        self.word = word
        self.index = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            startingChar = word[0]
            buckets[startingChar].append(Node(word))

        ans = 0
        for c in s:
            currBucket = buckets[c]
            buckets[c] = []
            for node in currBucket:
                node.index += 1  # Point to next character of node.word
                if node.index == len(node.word):
                    ans += 1
                else:
                    startingChar = node.word[node.index]
                    buckets[startingChar].append(node)
        return ans