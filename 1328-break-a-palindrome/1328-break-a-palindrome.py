class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        ret = list(palindrome)
        
        for idx, char in enumerate(ret):
            if char == 'a' or (len(ret) % 2 and idx == len(ret) // 2):
                continue
                
            ret[idx] = 'a'
            return ''.join(ret)
        
        ret[-1] = 'b'
        return ''.join(ret)