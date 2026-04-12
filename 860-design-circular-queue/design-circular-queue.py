class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [None] *self.k
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        if (self.rear + 1) % self.k == self.front:
            return False
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear+1) %self.k
        self.q[self.rear] = value
        return True


    def deQueue(self) -> bool:
        if self.rear ==-1:
            return False
        if self.rear == self.front:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % self.k
        return True

        

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]
    def Rear(self) -> int:
        if self.rear==-1:
            return -1
        return self.q[self.rear]
    def isEmpty(self) -> bool:
        return self.rear==-1

    def isFull(self) -> bool:
        return (self.rear+1) % self.k == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()