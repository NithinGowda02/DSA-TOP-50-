class Stack:
    def __init__(self):
        self.stack = []
        self.capacity = 4

    def push(self, ele):
        if len(self.stack) < self.capacity:
            self.stack.append(ele)
        else:
            print("Stack is Full!")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty")

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty")

    def view_stack(self):
        if self.stack:
            return self.stack   # return full stack
        else:
            print("Stack is empty")


st = Stack()
st.push("Pen")
st.push("Pencil")
print(st.view_stack())