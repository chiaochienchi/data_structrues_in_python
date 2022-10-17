# 只是存储工具，具体链接data和next要人来操作，新的节点存储这一个的next和下一个的data，像锁链一样
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext
