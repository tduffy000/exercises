from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque() # right == top

    def is_empty(self):
        return len(self.stack) == 0
        
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
        
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = Stack()
        open_char = {'(', '{', '['}
        close_char = {')': '(', '}': '{', ']': '['}        
        
        for ch in s:
            if ch in open_char:
                stack.push(ch)
            if ch in close_char:
                open_ch = stack.pop()
                if open_ch != close_char[ch]:
                    return False
        
        return stack.is_empty()
