# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        headNode = ListNode()
        p = headNode
        while(len(lists)):
            minVal = float("inf")
            minIdx = -1
            lists = [x for x in lists if x]
            if len(lists) == 0:
                break
            for i,x in enumerate(lists):
                if x.val < minVal:
                    minVal = x.val
                    minIdx = i
            q = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            p.next = q
            q.next = None
            p = q
        return headNode.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        head = ListNode()
        p = head
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val,i))
                lists[i] = lists[i].next
        while q:
            x, idx = heapq.heappop(q)
            p.next = ListNode(x)
            p = p.next
            if lists[idx]:
                heapq.heappush(q, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return head.next