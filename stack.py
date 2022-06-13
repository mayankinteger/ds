#last in first out (plates ka ghuccha)

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peep(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)


s = Stack()
s.push(10)
s.push(20)
print(s.container)
s.pop()
print(s.container)
s.push(50)
s.push(60)
print(s.peep())
print(s.is_empty())
print(s.size())
print(s.container)