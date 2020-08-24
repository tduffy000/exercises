# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode((l1.val + l2.val) % 10, None)
        h = newHead
        carry = int((l1.val + l2.val) >= 10)
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            rem = (l1.val + l2.val + carry) % 10
            carry = int((l1.val + l2.val + carry) >= 10)
            h.next = ListNode(rem, None)
            h = h.next
        while l1.next is not None:
            l1 = l1.next
            rem = (l1.val + carry) % 10
            carry = int((l1.val + carry) >= 10)
            h.next = ListNode(rem, None)
            h = h.next
        while l2.next is not None:
            l2 = l2.next
            rem = (l2.val + carry) % 10
            carry = int((l2.val + carry) >= 10)
            h.next = ListNode(rem, None)
            h = h.next
        if carry == 1:
            h.next = ListNode(carry, None)
        
        return newHead
        
