class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Pair:
    def __init__(self,node,state):
        self.node=node
        self.state=state

def Stack():
    stack=[]
    return stack
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Peek(s):
    return s[-1]

def inorder(root):
    stack=Stack()
    Push(stack,Pair(root,1))

    while(Size(stack)>0):
        top=Peek(stack)

        if top.state==1:
            top.state+=1
            if top.node.left!=None:
                lp=Pair(top.node.left,1)
                Push(stack,lp)


        elif top.state==2:
            top.state += 1
            print(top.node.val,end=' ')
            if top.node.right != None:
                rp = Pair(top.node.right, 1)
                Push(stack, rp)
            
        elif top.state==3:
            s=Pop(stack)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)