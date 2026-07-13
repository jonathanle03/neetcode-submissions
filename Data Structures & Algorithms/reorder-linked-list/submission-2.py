# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None or head.next.next == None:
            return

        # Slow is the midpoint
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        # Reverse the 2nd half of list
        curr = slow
        queue = []
        while curr:
            queue.append(curr)
            curr = curr.next
        
        new_head = None
        for node in queue:
            node.next = new_head
            new_head = node

        # Merge the two halves
        curr = head
        new_curr = new_head
        while curr:
            temp = curr.next
            curr.next = new_curr
            curr = temp

            if new_curr:
                temp = new_curr.next
                new_curr.next = curr
                new_curr = temp