# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: # 노드가 한개일때 삭제되어 None 리턴
            return None

        start = head
        # 노드의 수 total 을 구해 앞에서부터 몇번째 노드를 삭제할 것인지 구한다.
        total = 1
        while head.next:
            total += 1
            head = head.next
        index = total - n # 삭제할 노드의 인덱스

        head = start
        if index == 0: # 만약 첫번째 인덱스의 노드를 삭제한다면 head.next 를 리턴
            return head.next
        
        i = 0
        while head.next: # 중간에 있는 노드를 삭제시, 삭제하고자 하는 노드에 닿을때 head.next 를 그 다음 노드로 바로 연결한다.
            if i + 1 == index:
                head.next = head.next.next
                break
            i += 1
            head = head.next
        
        head = start
        return head
