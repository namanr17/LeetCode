class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        bitmask = 0
        
        for char in sentence:
            bitIdx = ord(char) - ord('a')
            bitmask |= (1 << bitIdx)
        
        return bitmask == (1 << 26) - 1