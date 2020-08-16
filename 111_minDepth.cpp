/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        if (root->left == NULL && root->right == NULL) return 1;
        int m1 = minDepth(root->left);
        int m2 = minDepth(root->right);
        if (root->left == NULL || root->right == NULL) return m1 + m2 + 1;
        return min(m1, m2) + 1;
    }
};
