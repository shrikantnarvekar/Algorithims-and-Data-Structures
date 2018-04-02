class Treenode:
    def __init__(self,d):
        self.data=d
        self.lchild=None
        self.rchild=None

class Mytree:

    def __init__(self,t):
        self.root=t

    def preorder(self,t):
        
        if t is not None:
            print(t.data)
            self.preorder(t.lchild)
            self.preorder(t.rchild)

    def inorder(self,t):
       
        if t is not None:
            self.inorder(t.lchild)
            print(t.data)
            self.inorder(t.rchild)

    def postorder(self,t):
       
        if t is not None:
            self.preorder(t.lchild)
            self.preorder(t.rchild)
            print(t.data)

    def conpreorder(self,t):
        
        if t is not None:
            print(t.data)
            self.preorder(t.rchild)
            self.preorder(t.lchild)

    def coninorder(self,t):
       
        if t is not None:
            self.inorder(t.rchild)
            print(t.data)
            self.inorder(t.lchild)

    def conpostorder(self,t):
       
        if t is not None:
            self.preorder(t.rchild)
            self.preorder(t.lchild)
            print(t.data)
F=Treenode("F")
B=Treenode("B")
K=Treenode("K")
A=Treenode("A")
B=Treenode("B")
D=Treenode("D")
C=Treenode("C")
G=Treenode("G")
F.lchild=B
F.rchild=K
B.lchild=A
B.rchild=D
D.lchild=C
K.lchild=G
mt=Mytree(F)
print("preorder: ")
mt.preorder(F)
print("inorder: ")
mt.inorder(F)
print("postorder: ")
mt.postorder(F)
print("converse preorder: ")
mt.conpreorder(F)
print("converse inorder: ")
mt.coninorder(F)
print("converse postorder: ")
mt.postorder(F)
