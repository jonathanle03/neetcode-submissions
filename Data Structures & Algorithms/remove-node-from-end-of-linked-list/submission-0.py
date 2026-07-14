# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        prev = None
        for i in range(length - n):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        
        return head
