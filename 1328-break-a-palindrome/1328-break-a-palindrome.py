class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:  return ''
        
        for idx, char in enumerate(palindrome):
            if idx == n-1 or char == 'a' or (n % 2 and idx == n // 2):
                continue
                
            return palindrome[:idx] + 'a' + palindrome[idx+1:]
        
        if palindrome[-1] == 'a':
            return palindrome[:-1] + 'b'
        else:   return palindrome[:-1] + 'a'