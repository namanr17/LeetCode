class StockSpanner:

    def __init__(self):
        self.idx = 0
        self.stack = deque([(0, float(inf))])

    def next(self, price: int) -> int:
        self.idx += 1
        while(self.stack[-1][1] <= price):
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)