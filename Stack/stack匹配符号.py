class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()


def strchecker(str1):
    s = Stack()
    blanced = True
    index = 0
    while index < len(str1) and blanced:
        if str1[index] in '([{':
            s.push(str1[index])
        else:
            if s.isempty():
                blanced = False
            elif match(str1[index], s.peek()):
                s.pop()
            else:
                blanced = False
        index += 1

    if blanced and s.isempty():
        return True
    else:
        return False


def match(x, y):
    if x in '{}' and y in '{}':
        return True
    elif x in '[]' and y in '[]':
        return True
    elif x in '()' and y in '()':
        return True
    else:
        return False


print(strchecker('{([])}'))
