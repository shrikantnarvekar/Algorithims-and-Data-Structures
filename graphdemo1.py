class GraphNode :
    def __init__(self,d):
        self.data = d
        self.status=0

class MyGraph :
    def __init__(self):
        self.nodelist=[]
        self.matrix = list()
        
    def addNodes(self):
        n = int (input("Enter how many nodes:"))
        
        for i in range(0,n) :           
            self.matrix.append(list())
            for j in range(0,n) :                
                self.matrix[i].append(0)            
            t = input("Enter a node :")
            g = GraphNode(t)
            g.status=0
            self.nodelist.append(g)
        
        
        
    def addEdge(self,edge):
            r=-1
            c=-1
            for i in range(len(self.nodelist)):
                if(self.nodelist[i].data == edge[0]) :
                    r=i
                if(self.nodelist[i].data == edge[1]) :
                    c=i
                
            if r==-1 or c==-1 :
                print("Invalid edge...")
            else:
                self.matrix[r][c] = 1

    def printGraph(self):
        for i in range(len(self.nodelist)):
            print(self.matrix[i])

    
    def bfs(self):
        templist = list()

        for i in range(len(self.nodelist)):
            self.nodelist[i].status = 1

        templist.append(self.nodelist[0])
        self.nodelist[0].status=2
        traversal = ""
        while(len(templist) != 0) :
            node = templist[0]
            templist.remove(node)
            traversal += node.data
            node.status = 3
            n = self.nodelist.index(node)            
            if(n>=0) :
                for t in range(0,len(self.nodelist)):
                    if self.matrix[n][t] ==1 and self.nodelist[t].status==1  :
                        templist.append(self.nodelist[t])
                        self.nodelist[t].status=2
            
        print(traversal)        

    def dfs(self):
        templist = list()

        for i in range(len(self.nodelist)+1):
            self.nodelist[i].status = 1

        templist.append(self.nodelist[0])
        self.nodelist[0].status=2
        traversal = ""
        while(len(templist) != 0) :
            node = templist[0]
            templist.remove(node)
            traversal += node.data
            node.status = 3
            n = self.nodelist.index(node)            
            if(n>=0) :
                for t in range(0,len(self.nodelist)+1):
                    if self.matrix[n][t] ==1 and self.nodelist[t].status==1  :
                        templist.append(self.nodelist[t]) #BFS
                        #templist.insert(0,self.nodelist[t]) #DFS
                        self.nodelist[t].status=2
            
        print(traversal)
        
g1=  MyGraph()
g1.addNodes()
n = int(input("how many edges? :"))
for i in range(0,n):
    edge = input("Enter edge :")
    g1.addEdge(edge)

g1.printGraph()
print("The BFS is:")
g1.bfs()
print("The DFS is:")
g1.dfs()
