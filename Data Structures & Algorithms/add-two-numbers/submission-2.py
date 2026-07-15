# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = None
        curr1 = l1
        curr2 = l2
        prev = None

        while curr1 and curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        
        longest = None
        if curr1:
            longest = l1
        else:
            longest = l2
        
        curr1 = l1
        curr2 = l2
        longest_curr = longest
        prev = None
        carry = 0

        while curr1 and curr2:
            old1 = curr1.val
            old2 = curr2.val
            longest_curr.val = (old1 + old2 + carry) % 10
            carry = (old1 + old2 + carry) // 10
            print(carry)
            prev = longest_curr
            curr1 = curr1.next
            curr2 = curr2.next
            longest_curr = longest_curr.next
        
        while longest_curr:
            old = longest_curr.val
            longest_curr.val = (old + carry) % 10
            carry = (old + carry) // 10
            print(carry)
            prev = longest_curr
            longest_curr = longest_curr.next
        
        if carry:
            node = ListNode(carry)
            prev.next = node

        
        return longest

        # while curr1 and curr2:
        #     node = ListNode((curr1.val + curr2.val + carry) % 10)
        #     if not sum:
        #         sum = node
        #     else:
        #         prev.next = node
        #     carry = (curr1.val + curr2.val + carry) // 10

        #     curr1 = curr1.next
        #     curr2 = curr2.next
        #     prev = node
        
        # while curr1:
        #     node = ListNode((curr1.val + carry) % 10)
        #     if not sum:
        #         sum = node
        #     else:
        #         prev.next = node
        #     carry = (curr1.val + carry) // 10
        #     curr1 = curr1.next
        #     prev = node
        
        # while curr2:
        #     node = ListNode((curr2.val + carry) % 10)
        #     if not sum:
        #         sum = node
        #     else:
        #         prev.next = node
        #     carry = (curr2.val + carry) // 10
        #     curr2 = curr2.next
        #     prev = node
        
        # if carry > 0:
        #     node = ListNode(carry)
        #     prev.next = node

        # return sum