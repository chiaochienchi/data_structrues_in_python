# list尾端是队列的前
class Deque:

    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)
    #     insert需要设置插入位置

    def removefront(self):
        return self.items.pop()
#     pop默认移除列表的最后一个元素

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
