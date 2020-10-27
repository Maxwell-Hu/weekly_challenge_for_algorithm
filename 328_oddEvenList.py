# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: return head
        p1 = head
        p2 = head.next
        l = head.next
        while p1.next and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            if p1.next == None:
                break
            p1 = p1.next
            p2 = p2.next
        p1.next = l
        return head
