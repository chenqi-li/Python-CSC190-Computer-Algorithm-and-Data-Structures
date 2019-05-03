class Queue:
    def __init__(self):
        self.lst = []
        self.cnt = 0

    def enqueue(self,x):
        self.lst = [x] + self.lst
        return True

    def dequeue(self):
        rm = self.lst[len(self.lst)-1]
        self.lst = self.lst[0:len(self.lst)-1]
        return rm

    def check(self):
        for i in self.lst:
            print(i)
        return True






def traverse_breath(T):
    x = Queue()
    for i in T:
        x.enqueue(i)
    while len(x.lst) != 0:
        r = x.dequeue()
        if type(r) == int:
            print(r)
        else:
            print(r[0])
            for i in r[1:len(r)]:
                x.enqueue(i)
        # print("After")
        # x.check()
    return True
