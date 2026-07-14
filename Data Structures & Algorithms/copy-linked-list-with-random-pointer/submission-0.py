"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        prev = None
        curr = head

        copies = {}

        while curr:
            node = Node(curr.val)
            copies[curr] = node

            if not new_head:
                new_head = node
            else:
                prev.next = node
            
            prev = node
            curr = curr.next
        
        for original, copy in copies.items():
            if original.random:
                copy_random = copies[original.random]
                copy.random = copy_random
        
        return new_head