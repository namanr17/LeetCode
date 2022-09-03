class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        dq = deque([str(i) for i in range(1, 10)])
        
        while(dq):
            num = dq.popleft()
            
            if len(num) == n:
                res.append(int(num))
                continue
            
            if int(num[-1]) - k >= 0:
                next_num = num + str(int(num[-1]) - k)
                dq.append(next_num)
            
            if k > 0 and int(num[-1]) + k < 10:
                next_num = num + str(int(num[-1]) + k)
                dq.append(next_num)
        
        return res