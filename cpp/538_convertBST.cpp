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
    int curSum = 0;
    TreeNode* convertBST(TreeNode* root) {
        postOrder(root);
        return root;
    }

    void postOrder(TreeNode *root){
        if (!root) return;
        postOrder(root->right);
        curSum += root->val;
        root->val = curSum;
        postOrder(root->left);
    }
};
