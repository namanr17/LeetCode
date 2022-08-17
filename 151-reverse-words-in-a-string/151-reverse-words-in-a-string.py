class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        refined = [''.join(word.split()) for word in words]
        refined = [word for word in words if len(word)]
        return ' '.join(refined[::-1])