class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')] 
        heapify(heap)
        
        ret = deque()
        while(heap):
            freq, char = heappop(heap)
            freq = -freq
            if len(ret) < 2 or ret[-1] != char:
                l = min(freq, 2)
                while(l):
                    ret.append(char)
                    l -= 1
                    freq -= 1
            
            if not heap:    break
            
            freq2, char2 = heappop(heap)
            if freq2:
                ret.append(char2)
                freq2 += 1
                heappush(heap, (freq2, char2))
            
            if freq:    heappush(heap, (-freq, char))
                
        return ''.join(list(ret))