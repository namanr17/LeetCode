class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        j = 0
        
        dominoes = ['L'] + list(dominoes) + ['R']
        
        for i in range(1, len(dominoes)):
            if dominoes[i] == '.':
                continue
                
            if dominoes[j] == dominoes[i]:
                for k in range(j, i):
                    dominoes[k] = dominoes[i]

            elif dominoes[i] == 'L' and i - j - 1 > 1:
                m = (i - j + 1) // 2
                for k in range(j, j+m):
                    dominoes[k] = 'R'
                
                for k in range(i, i-m, -1):
                    dominoes[k] = 'L'
            
            j = i
                
        return ''.join(dominoes[1:-1])