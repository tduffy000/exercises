# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        nodeI, nodeJ = head, head
        while nodeJ.next is not None:
            # increment nodeI once
            nodeI = nodeI.next
            
            # increment nodeJ twice
            nodeJ = nodeJ.next
            if nodeJ.next is None:
                break
            else:
                nodeJ = nodeJ.next
            
        return nodeI
