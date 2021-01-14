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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> p_path = getPath(root, p);
        vector<TreeNode*> q_path = getPath(root, q);
        TreeNode* res = root;
        for (int i=0; i<min(p_path.size(), q_path.size()); ++i) {
            if (p_path[i] == q_path[i]) res = p_path[i];
        }
        return res;
    }

    vector<TreeNode*> getPath(TreeNode* root, TreeNode* target) {
        vector<TreeNode*> path;
        TreeNode* node = root;
        while(node) {
            path.push_back(node);
            if (node->val == target->val) break;
            if (node->val > target->val) node = node->left;
            else node = node->right;
        }
        return path;
    }
};