class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = set(['+', '-', '*', '/'])
        
        for token in tokens:
            if token in ops:
                y = stack.pop()
                x = stack.pop()
                
                if token == '+':
                    res = x + y
                elif token == '-':
                    res = x - y
                elif token == '*':
                    res = x * y
                else:   res = int(float(x) / y)
                
                stack.append(res)
            else:   
                stack.append(int(token))
            # print(stack)
        
        return stack.pop()