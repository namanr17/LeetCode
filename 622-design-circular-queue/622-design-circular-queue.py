class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % self.max_size
            self.size -= 1
            return True
        

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1
        

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size