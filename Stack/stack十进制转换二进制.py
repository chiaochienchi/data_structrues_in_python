# 完蛋了，原理没看明白，写不了
# 明天再继续
# date：2022/9/9
# 原理是二进制可以写成C乘2的n次方求和的形式，不停取余则可得到对应位的数
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def divideby2(decnumber):
    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2

    binstring = ''
    while not remstack.isempty():
        binstring = binstring + str(remstack.pop())

    return binstring

