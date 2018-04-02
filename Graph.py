class Vertex:
  def __init__(self,n):
    self.node=n
    self.visited=False
    
  def setVertex(self,v):
    self.node=v
  def getVertex(self):
    return self.node

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def traverse(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print (n.value)
      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
    print
    thislevel = nextlevel

class Mygraph():
  def __init__(self):
    self.nodes=[]
    self.adjacency=[]
    self.first=None
    self.second=None
    
  def getNodes(self):
       for i in range (0,len(self.nodes)):
         print(self.nodes[i].node)
  def addNodes(self,nod):
        self.nodes.append(nod)
  def initAdjacency(self):
    for i in range(len(self.nodes)):
      temp=[]
      for j in range(len(self.nodes)):
        temp.append(0)
      self.adjacency.append(temp)
      
    print(self.adjacency)
      
  def addEdge(self,enm):
    self.first=enm[0]
    self.second=enm[1]
    id1=0
    id2=0
    for i in range(0,len(self.nodes)):
      if self.first==self.nodes[i].node:
        id1=i
        break
    for j in range(0,len(self.nodes)):
      if self.second==self.nodes[j].node:
        id2=j
        break
    self.adjacency[id1][id2]=1
   
  def printAdj(self):
    print(self.adjacency)
    print("------------------------------------------------------------------")
    
  def DfS_traverse():
    pass
    

mg=Mygraph()
i=int(input("Enter No of vertex:"))
for data in range(i):
  ip=Vertex(str(input("enter vertex:")))
  mg.addNodes(ip)


print("------------------------------GET NODES-----------------------------")
mg.getNodes()
print("------------------------------INIT ADJACENCY-----------------------------")

mg.initAdjacency()


for item in range(i-1):
  edge_name=str(input("enter edge:"))
  mg.addEdge(edge_name)
  mg.printAdj()

t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

traverse(t)
  
