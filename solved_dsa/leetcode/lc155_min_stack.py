
class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.main_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    
obj = MinStack()

minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())  
print(minStack.getMin())
