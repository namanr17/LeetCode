class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] >= 0 and a < 0: # collision happens
                collision = stack[-1] + a # collision result
                if collision <= 0: stack.pop() # stack top is destroyed
                if collision >= 0: break # new astroid is destroyed or both are destroyed
            else:
                stack.append(a)
        return stack