class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return self.stack == []

    def peek(self):
        return self.stack[len(self.stack)-1]

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)


def parchecker(list1):
    checker = Stack()
    index = 0
    balanced = True
    while index < len(list1) and balanced:
        if list1[index] == '(':
            checker.push(list1[index])
        elif list1[index] == ')':
            if checker.isempty():
                balanced = False
            else:
                checker.pop()
        index += 1

    if balanced and checker.isempty():
        return True
    else:
        return False

parString = '((())'
print(parchecker(parString))
