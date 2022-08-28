class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        buckets = Counter()
        
        for d in range(1-n, m):
            i, j = (0, -d) if d < 0 else (d, 0)
            
            while(i < m and j < n):
                buckets[mat[i][j]] += 1
                i += 1
                j += 1
                
            i, j = (0, -d) if d < 0 else (d, 0)
            k = 1
            
            while(k <= 100):
                while(buckets[k]):
                    mat[i][j] = k
                    buckets[k] -= 1
                    i += 1
                    j += 1
                k += 1
            
        return mat