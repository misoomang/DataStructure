class StackNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkStack:
    def __init__(self):
        self.top = StackNode()

    def is_empty(self):
        if not self.top.next:
            return True
        else:
            return False

    def push_stack(self, data):
        push_node = StackNode()
        push_node.data = data
        push_node.next = self.top.next
        self.top.next = push_node

    def pop_stack(self):
        if self.is_empty():
            return 'link stack is empty'
        else:
            e = self.top.data
            self.top = self.top.next
            return e

