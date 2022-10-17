class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([x for x in sentence])) == 26