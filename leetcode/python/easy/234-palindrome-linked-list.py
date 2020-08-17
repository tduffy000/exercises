# Definition for singly-linked list.
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        c = deque()
        if head is None:
            return True
        while head.next:
            c.append(head.val)
            head = head.next
        c.append(head.val)
            
        if len(c) % 2 == 0:
            while len(c) > 0:
                lend = c.popleft()
                rend = c.pop()
                if lend != rend:
                    return False
        else:
            while len(c) > 1:
                lend = c.popleft()
                rend = c.pop()
                if lend != rend:
                    return False
        return True
            
