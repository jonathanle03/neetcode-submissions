# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = None
        prev = None

        for i in range(n - 1):
            first = first.next
        
        while first:
            first = first.next
            prev = second
            if second:
                second = second.next
            else:
                second = head
        
        if prev:
            prev.next = second.next
        else:
            head = second.next

        return head
