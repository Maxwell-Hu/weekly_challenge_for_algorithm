# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val + l2.val + carry < 10:
                prev.next = ListNode(l1.val+l2.val+carry)
                carry = 0
            else:
                prev.next = ListNode((l1.val+l2.val+carry)%10)
                carry = 1
            l1 = l1.next
            l2 = l2.next
            prev = prev.next
        if l1:
            while l1:
                if l1.val + carry < 10:
                    prev.next = ListNode(l1.val+carry)
                    carry = 0
                else:
                    prev.next = ListNode(0)
                    carry = 1
                l1 = l1.next
                prev = prev.next
        else:
            while l2:
                if l2.val + carry < 10:
                    prev.next = ListNode(l2.val+carry)
                    carry = 0
                else:
                    prev.next = ListNode(0)
                    carry = 1
                l2 = l2.next
                prev = prev.next
        if carry:
            prev.next = ListNode(1)
        return prehead.next
