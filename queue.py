#first in first out (movie ticket line)


from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


s = Queue()
s.enqueue(10)
s.enqueue(20)
print(s.buffer)
s.dequeue()
print(s.buffer)
s.enqueue(50)
s.enqueue(60)
print(s.is_empty())
print(s.size())
print(s.buffer)