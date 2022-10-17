# 模拟打印任务，没看懂 9/14
class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(item)

    def dequeue(self):
        return self.items.pop()


def print1():
