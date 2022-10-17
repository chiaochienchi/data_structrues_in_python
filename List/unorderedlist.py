# 无序列表（unordered list）是基于节点集合来构建的，每一个节点都通过显式的
# 引用指向下一个节点。只要知道第一个节点的位置（第一个节点包含第一个元素），其后的每一
# 个元素都能通过下一个引用找到
from node import Node


class Unorderedlist:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        # current是节点
        found = None
        while not found and current is not None:
            if current.getdata == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        # 先找到要移除的节点item
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        # 找到结点之后修改节点前后的指针
        # 考虑要移除链表第一个节点的情形
        if previous is None:
            # 直接删掉第一个节点，把head改成current的下一个
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext)

    def append(self, item):

