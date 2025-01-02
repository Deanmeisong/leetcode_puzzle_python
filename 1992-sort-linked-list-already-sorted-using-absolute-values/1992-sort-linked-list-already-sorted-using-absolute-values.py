# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = head, head.next
        while curr:
            if curr.val < 0:
                t = curr.next
                pre.next = t
                curr.next = head
                head = curr
                curr = t
            else:
                pre, curr = curr, curr.next
        return head