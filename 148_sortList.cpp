/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* slow = head, *pre = head, *fast = head;
        while(fast && fast->next) {
            pre = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        pre->next = nullptr;
        return mergeTwoList(sortList(head), sortList(slow));
    }
    ListNode* mergeTwoList(ListNode* L1, ListNode* L2) {
        if(!L1) return L2;
        if(!L2) return L1;
        if(L1->val < L2->val) {
            L1->next = mergeTwoList(L1->next, L2);
            return L1;
        }
        else {
            L2->next = mergeTwoList(L1, L2->next);
            return L2;
        }
    }
};
