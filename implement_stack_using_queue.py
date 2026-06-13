from collections import deque

class stackQueue():
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q    

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]      

    def is_empty(self):
        return not self.q

stk = stackQueue()
stk.push(1)
stk.push(2)
stk.push(3)
print()
print(stk.top())
print(stk.pop())

       
