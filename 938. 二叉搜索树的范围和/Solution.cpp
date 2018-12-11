//
// Created by Ryan Shen on 2018-12-07.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// 利用递归来完成任务
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if (NULL == root)
            return 0;
        if (root->val > R) {
            return rangeSumBST(root->left, L, R);
        } else if (root->val <L) {
            return rangeSumBST(root->right, L, R);
        } else {
            return root->val + rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
        }
    }
};