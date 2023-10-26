# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Linked List, Two Pointer
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        
        empty = ListNode()
        cur = empty

        while head:
            if head.val not in dic:
                dic[head.val] = 1
            else:
                dic[head.val] += 1
            if head.next is None:
                break
            head = head.next

        for key in dic:
            if dic[key] == 1:
                cur.next = ListNode(key)
                cur = cur.next

        return empty.next

        