class queue:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def empty(self):
       if self.cnt==0:
          return True
       else:
          return False

    def add(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def retrieve(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[0]
            self.cnt=self.cnt-1
            self.store=self.store[1:]
            return [True,r]

class stack:
   def __init__(self):
      self.store=[]
      self.cnt=0

   def empty(self):
      if (self.cnt==0):
         return True
      else:
         return False

   def add(self,x):
      self.store = self.store + [x]
      self.cnt += 1
      return True

   def retrieve(self):
      if (self.cnt==0):
         return [False,0]
      else:
         self.cnt = self.cnt - 1
         rval = self.store[-1]
         self.store = self.store[:-1]
         return [True,rval]

class graph:
    def __init__(self):
        self.store = []

    def addVertex(self, n):
        for i in range(0,n):
            self.store += [[]]
        return len(self.store)

    def addEdge(self, from_idx, to_idx, directed, weight):
        #Check for error condition
        if from_idx >= len(self.store) or to_idx >= len(self.store):
            return False
        if directed != False and directed != True:
            return False

        #Add first way
        self.store[from_idx] += [[to_idx, weight]]
        #Check if second way is necessary
        if directed == False:
            self.store[to_idx] += [[from_idx, weight]]
        return True

    def traverse(self, start, typeBreadth):
        if typeBreadth == True:
            C = queue()
        elif typeBreadth == False:
            C = stack()
        D = [False] * len(self.store)
        P = list(D)
        rval = []


        if start == None:
            vertices = range(0, len(self.store))
        else:
            vertices = [start]


        for vertex in vertices:
            accum = []
            if D[vertex] == False:
                C.add(vertex)
                D[vertex] = True
            while(len(C.store) != 0):
                retrieve = C.retrieve()[1]
                if P[retrieve] == False:
                    accum += [retrieve]
                    P[retrieve] = True
                    for connections in self.store[retrieve]:
                        if D[connections[0]] == False:
                            C.add(connections[0])
                            D[connections[0]] = True
            if start != None:
                return accum
            if len(accum) != 0:
                rval = rval + [accum]
        return rval

    def connectivity(self, vx, vy):
        connected_vertices = self.traverse(vx,False)
        wayone = False
        for i in connected_vertices:
            if vy == i:
                wayone = True


        connected_vertices = self.traverse(vy, False)
        waytwo = False
        for i in connected_vertices:
            if vx == i:
                waytwo = True

        return [wayone, waytwo]

    def direct_connection(self,vx,vy):
        for i in self.store[vx]:
            if i[0] == vy:
                return True
        else:
            return False

    def path(self, vx, vy):
        if vx == vy:
            print("ERR: Start and End should be different")
            return False
        way = self.connectivity(vx,vy)

        #Case 1: no path between two
        if way[0] == False and way[1] == False:
            return [[],[]]

        #Case 2: second to first path only
        elif (way[0] == False) and (way[1] == True):
            paths = self.traverse(vy, False)
            #Clean up List
            i = 0
            while i < len(paths)-1:
                if self.direct_connection(paths[i],paths[i+1]) == False and paths[i] != vx:
                    paths = paths[0:i] + paths[i+1:]
                else:
                    i+=1
            #Find path
            for i in range(0, len(paths), 1):
                if paths[i] == vy:
                    start = i
                if paths[i] == vx:
                    end = i
            return [[],paths[start:end+1]]

        #Case 3: first to second path only
        elif way[0] == True and way[1] == False:
            paths = self.traverse(vx, False)
            #Clean up list
            i = 0
            while i < len(paths)-1:
                if self.direct_connection(paths[i],paths[i+1]) == False and paths[i] != vy:
                    paths = paths[0:i] + paths[i+1:]
                else:
                    i+=1
            #Find path
            for i in range(0, len(paths), 1):
                if paths[i] == vx:
                    start = i
                if paths[i] == vy:
                    end = i
            return [paths[start:end+1],[]]

        #Case 4: both ways
        else:
            #way 1
            paths = self.traverse(vx, False)
            #Clean up list
            i = 0
            while i < len(paths)-1:
                if self.direct_connection(paths[i],paths[i+1]) == False and paths[i] != vy:
                    paths = paths[0:i] + paths[i+1:]
                else:
                    i+=1
            #Find path
            for i in range(0, len(paths), 1):
                if paths[i] == vx:
                    start = i
                if paths[i] == vy:
                    end = i

            #way 2
            path = self.traverse(vy, False)
            #Clean up list
            j = 0
            while j < len(path)-1:
                if self.direct_connection(path[j],path[j+1]) == False and path[j] != vx:
                    path = path[0:j] + path[j+1:]
                else:
                    j+=1
            #Find path
            for j in range(0, len(path), 1):
                if path[j] == vy:
                    strt = j
                if path[j] == vx:
                    ed = j
            return [paths[start:end+1], path[strt:ed+1]]

x = graph()
x.addVertex(10)
x.addEdge(0, 1, True, 0.1)
x.addEdge(0, 2, True, 0.1)
x.addEdge(0, 3, True, 0.9)
x.addEdge(1, 2, False, 0.4)
x.addEdge(1, 5, False, 0.2)
x.addEdge(3, 5, False, 0.5)
x.addEdge(3, 2, True, 0.3)
x.addEdge(5, 2, True, 0.7)
x.addEdge(4, 6, False, 1.5)
x.addEdge(8, 9, True, 7.0)

print(x.store)
print(x.traverse(0, False))
print(x.path(2, 5))


"""
#addEdge first interpretation
        #Undirected
        if directed == True:
            for node in self.store:
                if node != []:
                    if node[0] == from_idx:
                        node += [[to_idx, weight]]
                        break
            else:
                for node in self.store:
                    if node == []:
                        node += [from_idx]
                        node += [[to_idx, weight]]
                        break
        #Directed
        else:
            #First way
            for node in self.store:
                if node != []:
                    if node[0] == from_idx:
                        node += [[to_idx, weight]]
                        break
            else:
                for node in self.store:
                    if node == []:
                        node += [from_idx]
                        node += [[to_idx, weight]]
                        break

            #Second way
            for node in self.store:
                if node != []:
                    if node[0] == to_idx:
                        node += [[from_idx, weight]]
                        break
            else:
                for node in self.store:
                    if node == []:
                        node += [to_idx]
                        node += [[from_idx, weight]]
                        break
"""
