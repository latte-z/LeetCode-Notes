# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = TreeNode(None)
        self.myQueue = []

    def add(self, val):
        node = TreeNode(val)
        # 根节点空，则取出list的值进行赋值
        if self.root.val is None:
            self.root = node
            self.myQueue.append(self.root)
        else:
            # 对节点的子树进行赋值
            tree_node = self.myQueue[0]
            if tree_node.left is None:
                tree_node.left = node
                self.myQueue.append(tree_node.left)
            else:
                tree_node.right = node
                self.myQueue.append(tree_node.right)
                # 如果存在了右节点则丢弃
                self.myQueue.pop(0)

    def delete_none_node(self, root):
        if root is None:
            return
        if root.left is not None:
            if root.left.val is None:
                root.left = None
            else:
                self.delete_none_node(root.left)
        if root.right is not None:
            if root.right.val is None:
                root.right = None
            else:
                self.delete_none_node(root.right)

    def level_ergodic(self, root):
        if root is None:
            return
        my_queue = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print(node.val)
            if node.left is not None:
                my_queue.append(node.left)
            if node.right is not None:
                my_queue.append(node.right)

    def middle_ergodic(self, root):
        if root is None:
            return
        self.middle_ergodic(root.left)
        print(root.val)
        self.middle_ergodic(root.right)


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent_tree_dict = {}
        self.set_parent_tree_node(root, parent_tree_dict, None)
        leaf_list = []
        max_level = self.get_depth(root)
        if max_level == 1:
            return root
        self.get_leaf_node(leaf_list, root, 1, max_level)
        if len(leaf_list) == 1:
            return leaf_list[0]
        else:
            while len(leaf_list) > 1:
                leaf_list_len = len(leaf_list)
                for i in range(0, leaf_list_len):
                    tree_node = leaf_list[i]
                    leaf_list.pop(i)
                    leaf_list.insert(i, parent_tree_dict[tree_node])
                while len(leaf_list) > 1:
                    if leaf_list[0] == leaf_list[1]:
                        leaf_list.pop(0)
                    else:
                        break
        return leaf_list[0]

    def get_depth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        return right + 1 if left < right else left + 1

    def get_leaf_node(self, leaf_node_list, root, level, max_level):
        if root is None:
            return
        if level == max_level:
            if root is not None:
                leaf_node_list.append(root)
            return
        self.get_leaf_node(leaf_node_list, root.left, level + 1, max_level)
        self.get_leaf_node(leaf_node_list, root.right, level + 1, max_level)

    def set_parent_tree_node(self, root, parent_tree_node_dict, parent):
        if root is None:
            return
        if parent is not None:
            parent_tree_node_dict[root] = parent
        self.set_parent_tree_node(root.left, parent_tree_node_dict, root)
        self.set_parent_tree_node(root.right, parent_tree_node_dict, root)


if __name__ == '__main__':
    inputTreeNode = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    tree = Tree()
    for item in inputTreeNode:
        tree.add(item)
    tree.delete_none_node(tree.root)
    solution = Solution()
    tree.level_ergodic(solution.subtreeWithAllDeepest(tree.root))
