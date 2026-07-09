# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = res
        node1 = list1
        node2 = list2

        while node1 and node2:
            if node1.val < node2.val:
                if curr == None:
                    curr = node1
                    res = curr
                else:
                    curr.next = node1
                    curr = curr.next
                node1 = node1.next
            else:
                if curr == None:
                    curr = node2
                    res = curr
                else:
                    curr.next = node2
                    curr = curr.next
                node2 = node2.next
        
        if node1:
            if curr == None:
                curr = node1
                res = curr
            else:
                curr.next = node1

        if node2:
            if curr == None:
                curr = node2
                res = curr
            else:
                curr.next = node2

        return res