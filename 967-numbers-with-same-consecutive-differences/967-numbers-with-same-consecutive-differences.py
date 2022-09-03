class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        dq, res = deque([i for i in range(1, 10)]), []
        
        while(dq):
            num = dq.popleft()
            
            if int(log10(num)) + 1 == n:
                res.append(num)
                continue
            
            last_digit = num % 10
            for next_digit in set([last_digit - k, last_digit + k]):
                if 0 <= next_digit < 10:
                    dq.append(num * 10 + next_digit)
        
        return res