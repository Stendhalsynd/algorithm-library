# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Linke List, Two Pointers
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head
        total = 1

        if not fast or not fast.next:
            return head

        while fast.next:
            total += 1
            fast = fast.next
        if k > total:
            k %= total
        fast = head

        if total == k:
            return head

        for i in range(k):
            if fast.next:
                fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head