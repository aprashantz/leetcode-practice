class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack2) > 0:
            temp = self.stack2.pop()
            self.stack1.append(temp)
        self.stack1.append(x)
        while len(self.stack1) > 0:
            temp = self.stack1.pop()
            self.stack2.append(temp)

    def pop(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2.pop()
        else:
            return 0

    def peek(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2[len(self.stack2)-1]
        else:
            0

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# test below
queue1 = MyQueue()
queue1.push(1)
queue1.push(2)
queue1.push(3)
queue1.pop()
