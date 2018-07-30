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


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.pruneTree(root.left) and self.pruneTree(root.right):
            return


if __name__ == '__main__':
    solution = Solution()
    input_tree_node = [1, 0, 1, 0, 0, 0, 1]
    tree = Tree()
    for item in input_tree_node:
        tree.add(item)
    solution.pruneTree(tree.root)
