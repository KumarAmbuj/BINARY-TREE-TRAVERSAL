class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Pair():
    def __init__(self,node,s):
        self.node=node
        self.s=s

def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Peek(s):
    return s[-1]

def preorder(node):
    s=Stack()
    Push(s,Pair(node,1))

    while(Size(s)):

        top=Peek(s)

        if top.s==1:
            print(top.node.val,end=' ')
            top.s+=1
            if top.node.left:
                np=Pair(top.node.left,1)
                Push(s,np)

        elif top.s==2:
            top.s += 1
            if top.node.right:
                np = Pair(top.node.right, 1)
                Push(s, np)

        elif top.s==3:
            x=Pop(s)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
preorder(root)

