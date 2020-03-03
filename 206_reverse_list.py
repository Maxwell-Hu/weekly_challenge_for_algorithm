# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reversedList = ListNode(0)
        while(head):
            newNode = ListNode(head.val)
            newNode.next = reversedList.next
            reversedList.next = newNode
            head = head.next
        return reversedList.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
