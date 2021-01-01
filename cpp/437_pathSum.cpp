/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        unordered_map<int, int> store;
        return help(root, store, sum, 0);
    }

    int help(TreeNode* root, unordered_map<int, int>& store, int target, int curSum){
        if (!root) return 0;
        curSum += root->val;
        int res = (curSum == target) + (store.count(curSum - target) ? store[curSum - target] : 0);
        store[curSum]++;
        int l = help(root->left, store, target, curSum);
        int r = help(root->right, store, target, curSum);
        res += l + r;
        store[curSum]--;
        return res;
    }
};
