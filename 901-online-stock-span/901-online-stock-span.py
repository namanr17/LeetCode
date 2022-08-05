class StockSpanner:

    def __init__(self):
        self.idx = 0
        self.arr = [float(inf)]
        self.stack = deque([0])

    def next(self, price: int) -> int:
        self.idx += 1
        top = self.stack[-1]
        while(self.arr[top] <= price):
            self.stack.pop()
            top = self.stack[-1]
        self.stack.append(self.idx)
        self.arr.append(price)
        return self.idx - top
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)