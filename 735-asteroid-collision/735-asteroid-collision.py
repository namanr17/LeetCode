class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        ret = []
        
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
                continue
                
            while stack and stack[-1] < abs(ast):
                stack.pop()
            
            if not stack:
                ret.append(ast)
            elif abs(ast) == stack[-1]:
                stack.pop()
        
        for ast in stack:
            ret.append(ast)
            
        return ret