# Linked List, Math, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumLinkedList = ListNode(0)
        current = sumLinkedList

        s1, s2 = [], []
        s1.append(l1.val)
        s2.append(l2.val)
        
        while l1.next != None:
            l1 = l1.next
            s1.append(l1.val)
        while l2.next != None:
            l2 = l2.next
            s2.append(l2.val)

        v1 = int(''.join([str(s1.pop()) for _ in range(len(s1))]))
        v2 = int(''.join([str(s2.pop()) for _ in range(len(s2))]))
        result = list(map(int, str(v1 + v2)))
        
        for _ in range(len(result)):
            current.next = ListNode(result.pop())
            current = current.next
        
        return sumLinkedList.next