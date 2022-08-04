class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits)-1
        
        while(i > 0 and digits[i] <= digits[i-1]):
            i -= 1
        
        if i == 0:
            return -1
        
        j = i
        while j+1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))
        
        return -1 if ret > (2**31)-1 else ret