# 将字符串转换为列表
# 列表两端同时移除元素，并比较，若不相同则不是回文
# 最后只剩下一个或者空列表时，字符为回文
class Deque:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def huiwendetector(str1):
    ch = Deque()

    for i in str1:
        ch.addrear(i)

    stillequll = True

    while ch.size() > 1 and stillequll:
        first = ch.removefront()
        last = ch.removerear()
        if first != last:
            stillequll = False

    return stillequll


mystr = 'abcdedcba'
mystr1 = 'asdfghj'
print(huiwendetector(mystr))
print(huiwendetector(mystr1))
