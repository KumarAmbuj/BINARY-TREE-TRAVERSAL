class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)

def postorder(node):
    s1=Stack()
    s2=Stack()

    Push(s1,node)

    while(Size(s1)):
        rem=Pop(s1)

        Push(s2,rem)

        if rem.left:
            Push(s1,rem.left)
        if rem.right:
            Push(s1,rem.right)

    while(Size(s2)):
        print(Pop(s2).val,end=' ')

def posorder(node):
    if node:
        posorder(node.left)
        posorder(node.right)
        print(node.val,end=' ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postorder(root)
print()
posorder(root)
