class Mytree:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def preOrder(root):
   if root:
       print (root.data)
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print (root.data)
       
def conversepre(root):
    if root:
        print(root.data)
        conversepre(root.right)
        conversepre(root.left)

def conversepost(root):
    if root:
        conversepre(root.right)
        print(root.data)
        conversepre(root.left)

def conversein(root):
    if root:
        conversepre(root.right)
        conversepre(root.left)
        print(root.data)
    
#making the tree 
root = Mytree("A")
root.left = Mytree("B")
root.right = Mytree("C")
root.left.left = Mytree("D")
root.left.right = Mytree("E")
print("inorder")
print (inOrder(root))
print("preorder")
print (preOrder(root))
print("postorder")
print (postOrder(root))
print("conversepreorder:\n",conversepre(root))
print("conversepostorder:\n",conversepost(root))
print("converseinorder:\n",conversein(root))



