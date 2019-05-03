

class Stack:
    def __init__(self):
        self.lst = []
        self.cnt = 0

    def push(self, x):
        self.lst = [x] + self.lst
        self.cnt += 1
        return True

    def pop(self):
        print(self.cnt)

        if (self.cnt== 0):
            return [False, -1]
        else:
            self.rt = self.lst[0]
            self.lst = self.lst[1:]
            self.cnt -= 1
            return [True, self.rt]
"""
    def check(self):
        for i in self.lst:
            print(i)


g = Stack()
g.push(5)
g.check()
[a,b]=g.pop()
print("b is", b)
g.check()
[c,d] = g.pop()
print("c is", c)
"""


