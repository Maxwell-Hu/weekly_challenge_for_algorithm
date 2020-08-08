# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(0)
        p.next = head
        left, right = p, p
        for _ in range(n+1):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return p.next
