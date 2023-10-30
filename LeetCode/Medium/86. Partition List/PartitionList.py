# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node = ListNode()
        start = node
        cur = head

        greaterThenOrEqual = ListNode()
        start2 = greaterThenOrEqual

        while cur:
            if cur.val < x:
                node.next = ListNode(cur.val)
                node = node.next
            elif cur.val >= x:
                greaterThenOrEqual.next = ListNode(cur.val)
                greaterThenOrEqual = greaterThenOrEqual.next

            if cur.next is None:
                break
            cur = cur.next

        if node.next is None:
            node.next = start2.next

        return start.next