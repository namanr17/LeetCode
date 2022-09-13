class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def valid(i):
            return i < len(data) and (128 <= data[i] % 256 < 192)
        
        i = 0
        while(i < len(data)):
            x = data[i] % 256
            if 0 <= x < 128:
                i += 1
            elif 192 <= x < 224 and valid(i+1):
                i += 2
            elif 194 <= x < 240 and valid(i+1) and valid(i+2):
                i += 3
            elif 240 <= x < 248 and valid(i+1) and valid(i+2) and valid(i+3):
                i += 4
            else:   break
        
        return True if i == len(data) else False