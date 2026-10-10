#Arnau Teruel Gonzalez, 1796553

class MinStack:

    def __init__(self):
        self.stack = []      
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



s = MinStack()

s.push(-234356778686)
s.push(676767)
print(s.top())
print(s.pop())
print(s.top())
s.push(-78787878795950302847852)
s.push(-9934886790887887857456)
s.push(-23456789098765432)
print(s.getMin())
