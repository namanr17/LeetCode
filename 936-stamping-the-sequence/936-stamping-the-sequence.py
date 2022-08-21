class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ans = []
        len_S, len_T = len(stamp), len(target)
        S, T = list(stamp), list(target)
        
        def update(i):
            updated = False
            for j in range(len_S):
                if T[i+j] == '?':   continue
                if T[i+j] != S[j]:  return False
                updated = True
            
            if updated:
                T[i:i+len_S] = ['?'] * len_S
                ans.append(i)
                
            return updated
        
        
        updated = True    
        while updated:
            updated = False
            for i in range(len_T - len_S + 1):
                updated |= update(i)
            
        return ans[::-1] if T == ['?'] * len_T else []