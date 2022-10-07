class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }
        
        def convert(num):
            if not num: return ''
            
            base = 10 ** floor(log10(num))
            x = num // base
            
            if x in {4, 9}:
                return roman[base] + roman[(x+1) * base] + convert( num % base )
            
            buff = ''
            while( x * base not in roman ):
                buff += roman[base]
                x -= 1
            
            return roman[x * base] + buff[::-1] + convert( num % base )
        
        return convert(num)