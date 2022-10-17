# 实现堆这种抽象数据结构
# 假设list的尾部是栈的顶端
# 这种的时间的复杂度是O(1)
# 还有一种假设list的头部是栈的顶端
# 时间复杂度是O(n)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

