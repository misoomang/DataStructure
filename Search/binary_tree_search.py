# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class BTS:
    """
    创建二叉查找树：若左子树不为空，左子树上的节点值均小于根节点值
                    若右子树不为空，右子树上的节点值均大于根节点值
                    其左右子树也为二叉查找树
    """
    def __init__(self):
        self.root = Node()

    def search_num(self, node, parent, elem):
        if node is None:
            return False, node, parent
        if node.elem == elem:
            return True, node, parent
        if node.elem < elem:
            return self.search_num(node.right, node, elem)
        else:
            return self.search_num(node.left, node, elem)

    def insert_num(self, elem):
        if self.root.elem is None:
            self.root = Node(elem)
        else:
            flag, node, parent = self.search_num(self.root, self.root, elem)
            if not flag:
                new_node = Node(elem)
                if elem < parent.elem:
                    parent.left = new_node
                else:
                    parent.right = new_node

    def delete_num(self, elem):
        flag, node, parent = self.search_num(self.root, self.root, elem)
        if not flag:
            return False
        else:
            if node.left is None and node.right is None:        # 叶子节点
                parent.left = None
                parent.right = None
            elif node.left is None and node.right:  # 没有左孩子，有右孩子
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right
            elif node.right is None and node.left:  # 没有右孩子，有左孩子
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:           # 左右子树都不为空
                pre = node.right
                if pre.left is None:
                    node.elem = pre.elem
                    node.right = pre.right
                    del pre
                else:
                    next_node = node.left
                    while next_node:
                        pre = next_node
                        next_node = next_node.right
                    node.data = next_node.data
                    pre.right = next_node.left
            return True

    def find_min(self, root):
        """
        查找最小值
        :param root:
        :return:
        """
        if root.left:
            return self.find_min(root.left)
        else:
            return root.elem

    def find_max(self, root):
        """
        查找最大值
        :param root:
        :return:
        """
        if root.right:
            return self.find_max(root.right)
        else:
            return root.elem

    @staticmethod
    def level_recursive(root):
        if root is None:
            return
        node = root
        node_queue = list()
        node_queue.append(node)
        while node_queue:
            node = node_queue.pop(0)
            if node.elem is not None:
                print(node.elem)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)


if __name__ == '__main__':
    tree = BTS()
    for i in [62, 88, 58, 47, 35, 73, 51, 99, 37, 93]:
        tree.insert_num(i)
    # tree.level_recursive(tree.root)
    # print('max:', tree.find_max(tree.root))
    # print('min:', tree.find_min(tree.root))
    print(tree.delete_num(47))
    tree.level_recursive(tree.root)
