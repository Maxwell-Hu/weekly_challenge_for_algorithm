# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head == None:
            return head
        headNode = ListNode(0)
        headNode.next = head
        num, p = 0, headNode.next
        while p:
            num += 1
            p = p.next
        k = k % num
        pre, p = head, head
        count = 0
        while p:
            if count > k:
                pre = pre.next
            count += 1
            p = p.next
        q = headNode
        while pre.next:
            tmp = pre.next
            pre.next = tmp.next
            tmp.next = q.next
            q.next = tmp
            q = q.next
        return headNode.next
