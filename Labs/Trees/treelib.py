#Partially completed with consultation & help of solutions posted on design.engsci.utoronto.ca

from ex_4 import *

class tree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):
      self.Print_DF_Help('')
      return True

   def Print_DF_Help(self, pf):
      print (pf, self.store[0])
      for i in self.store[1]:
         i.Print_DF_Help(pf + " ")

   def Get_LevelOrder(self):
      x = Queue()
      for i in self.store:
          x.enqueue(i)
      #print("1 x.check()")
      #x.check()

      accum = []

      r = x.dequeue()
      #print("first r", r)

      accum += [r]
      #print("first accum", accum)

      while len(x.lst) != 0:
         r = x.dequeue()
         #print("r", r)
         #print("type(r)", r)
         if type(r) == list:
            for i in r:
               x.enqueue(i)
         else:
            #print(r.store[0])
            accum += [r.store[0]]
            #print(r.store[1])
            for i in r.store[1]:
               x.enqueue(i)
      # print("accum final:",accum)
      return accum

   def ConvertToBinaryTree(self, Sibs):
      Root = self.store[0]

      #Check for successors and their siblings
      if len(self.store[1]) == 0:
         L = []
      else:
         if len(self.store[1]) == 1:
            LSibs = []
         else:
            LSibs = self.store[1][1:]
         L = self.store[1][0].ConvertToBinaryTree(LSibs)

      #Check for siblings and their siblings
      if Sibs == []:
         R = []
      else:
         if len(Sibs) == 1:
            RSibs = []
         else:
            RSibs = Sibs[1:]
         R = Sibs[0].ConvertToBinaryTree(RSibs)

      #Make the Tree
      btree = binary_tree(Root)
      if L != []:
         btree.AddLeft(L)
      if R != []:
         btree.AddRight(R)
      return btree



class binary_tree:
   def __init__(self,x):
      self.store = [x]

   def AddLeft(self,x):
      self.store += [x]
      return True

   def AddRight(self,x):
      self.store += [x]
      return True

   def Get_LevelOrder(self):
      x = Queue()
      for i in self.store:
         x.enqueue(i)

      acc = []
      r = x.dequeue()
      acc += [r]

      while len(x.lst) != 0:
         r = x.dequeue()
         acc += [r.store[0]]
         if len(r.store) > 1:
            for i in r.store[1:]:
               x.enqueue(i)
      return acc

   def ConvertToTree(self):
      return self.store




'''
x=tree(1000)
y=tree(2000)
z=tree(3000)
x.AddSuccessor(y)
x.AddSuccessor(z)
c=tree(5)
z.AddSuccessor(c)
#x.Print_DepthFirst()
print(x.Get_LevelOrder())





x=binary_tree(1)
#print(x.store)
x.AddLeft(binary_tree(2))
#print(x.store[1])
y=binary_tree(3)
#print(y.store)
y.AddLeft(binary_tree(4))
#print(y.store)
y.AddRight(binary_tree(5))
#print(y.store)
x.AddRight(y)
x.Get_LevelOrder()
'''


