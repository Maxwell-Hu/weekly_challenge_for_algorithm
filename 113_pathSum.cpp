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
    vector<vector<int>> ret;
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        dfs(root, path, sum);
        return ret;
    }

    void dfs(TreeNode* root, vector<int> path, int sum) {
        if(root == nullptr) return;
        path.emplace_back(root->val);
        if(root->left == nullptr && root->right == nullptr) {
            if(accumulate(path.begin(), path.end(), 0) == sum) {
                ret.emplace_back(path);
            }
        }
        else {
            dfs(root->left, path, sum);
            dfs(root->right, path, sum);
        }
    }
};
