class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = [None] * k
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.arr[self.end] = value
        self.end = (self.end + 1) % self.k
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.k
        return True

    def Front(self) -> int:
        return self.arr[self.start] if self.arr[self.start] != None else -1

    def Rear(self) -> int:
        return self.arr[self.end - 1] if self.arr[self.end - 1] != None else -1

    def isEmpty(self) -> bool:
        return self.start == self.end and self.arr[self.start] == None

    def isFull(self) -> bool:
        return self.start == self.end and self.arr[self.start] != None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()