class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next


class LinkList:
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

    def is_empty(self):
        if not self._length:
            return True
        else:
            return False

    def add(self, value):
        new_node = Node(value, None)
        new_node.set_next(self._head)
        self._head = new_node
        self._length += 1

    def append(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            # 找到最后一个节点
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self._length += 1

    def search(self, value):
        current = self._head
        flag = False
        while current is not None and not flag:
            if current.get_value() == value:
                flag = True
            else:
                current = current.get_next()
        return flag

    def get_index(self, value):
        current = self._head
        flag = False
        count = 0
        while current is not None and not flag:
            count += 1
            if current.get_value() == value:
                flag = True
            else:
                current = current.get_next()

        if flag:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % value)

    def remove(self, value):
        current = self._head
        pre = None
        flag = False
        while current is not None:
            if current.get_value() == value:
                if not pre:
                    self._head = current.get_next()
                else:
                    pre.set_next(current.get_next())
                self._length -= 1
                flag = True
                break
            else:
                pre = current
                current = current.get_next()

        if flag:
            return 'remove %s successfully' % value
        else:
            raise ValueError('remove %s failed' % value)

    def insert(self, pos, value):
        if pos <= 1:
            self.add(value)
        elif pos >= self._length:
            self.append(value)
        else:
            tmp = Node(value)
            pre = None
            count = 1
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.get_next()
            if pre:
                pre.set_next(tmp)
                tmp.set_next(current)
