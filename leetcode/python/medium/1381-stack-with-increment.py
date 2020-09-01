from collections import deque

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize    
        self.stack = deque() # top is left
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.appendleft(x)
        return 
        
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.popleft()

    def increment(self, k: int, val: int) -> None:
        ops = min(k, len(self.stack))
        for i in reversed(range(len(self.stack)-ops, len(self.stack))):
            self.stack[i] += val
        return


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
