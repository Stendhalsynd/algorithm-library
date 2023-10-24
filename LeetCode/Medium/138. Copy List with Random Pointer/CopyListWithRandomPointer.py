# Hash Table, Linked List
import random
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
        if not head:
            return None

        copy = {}
        cur = head
        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                copy[cur].next = copy[cur.next]
            if cur.random:
                copy[cur].random = copy[cur.random]
            cur = cur.next

        return copy[head]