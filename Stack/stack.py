class Stack:
    def __init__(self, size=100):
        self.size = size
        self.stack = []
        self.top = -1

    def is_full(self):
        return self.size == self.top + 1

    def is_empty(self):
        return self.top == -1

    def stack_push(self, number):
        if self.is_full():
            raise ValueError('stack is full')
        else:
            self.stack.append(number)
            self.top += 1

    def stack_pop(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        else:
            pop_num = self.stack.pop()
            self.top -= 1
            return pop_num

    def stack_show(self):
        return self.stack


if __name__ == '__main__':
    stack = Stack(size=10)
    stack.stack_push(2)
    stack.stack_push(3)
    stack.stack_push(4)
    stack.stack_push(5)
    print(stack.stack_show())
