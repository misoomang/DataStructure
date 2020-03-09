# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem=elem)
        if self.root.elem == -1:        # 添加头节点
            self.root = node
            self.myQueue.append(node)
        else:
            tree_node = self.myQueue[0]
            if tree_node.left is None:      # 左孩子节点构建
                tree_node.left = node
                self.myQueue.append(tree_node.left)
            else:                           # 右孩子节点构建
                tree_node.right = node
                self.myQueue.append(tree_node.right)
                self.myQueue.pop(0)

    # 层次遍历
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
                # print(node.elem)
                yield node.elem
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)

    # 递归前序遍历
    def left_recursive(self, root):
        if root is None:
            return
        if root.elem is not None:
            # yield root.elem
            print(root.elem)
        self.left_recursive(root.left)
        self.left_recursive(root.right)

    # 非递归前序遍历(根左右)
    @staticmethod
    def left_recursive_1(root):
        if root is None:
            return
        node_queue = []
        node = root
        while node or node_queue:
            while node:             # 遍历左子树节点
                # print(node.elem)
                yield node.elem
                node_queue.append(node)
                node = node.left
            node = node_queue.pop()
            node = node.right

    # 中序遍历(左根右)
    @staticmethod
    def middle_recursive(root):
        if root is None:
            return
        node_queue = []
        node = root
        while node or node_queue:
            while node:
                node_queue.append(node)
                node = node.left
            node = node_queue.pop()
            # print(node.elem)
            yield node.elem
            node = node.right

    # 后续遍历(左右根)
    @staticmethod
    def last_recursive(root):
        if root is None:
            return
        node_queue_1 = []
        node_queue_2 = []
        node = root
        node_queue_1.append(node)
        while node_queue_1:
            node = node_queue_1.pop()
            if node.left:
                node_queue_1.append(node.left)
            if node.right:
                node_queue_1.append(node.right)
            node_queue_2.append(node)
        while node_queue_2:
            node = node_queue_2.pop()
            yield node.elem
            # print(node.elem)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 10):
        tree.add(i)
    level_recursive_list = []
    for i in tree.level_recursive(tree.root):
        level_recursive_list.append(i)
    print('层次遍历：', level_recursive_list)

    left_recursive_list = []
    for i in tree.left_recursive_1(tree.root):
        left_recursive_list.append(i)
    print('非递归先序遍历：', left_recursive_list)

    middle_recursive_list = []
    for i in tree.middle_recursive(tree.root):
        middle_recursive_list.append(i)
    print('中序遍历：', middle_recursive_list)

    last_recursive_list = []
    for i in tree.last_recursive(tree.root):
        last_recursive_list.append(i)
    print('后序遍历：', last_recursive_list)

    # print('递归先序遍历：')
    # print(tree.left_recursive(tree.root))

    # print('中序遍历：')
    # print(tree.middle_recursive(tree.root))
    # print('后序遍历：')
    # print(tree.last_recursive(tree.root))
