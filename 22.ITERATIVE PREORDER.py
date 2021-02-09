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

def preorder(node):
    s=Stack()
    Push(s,node)
    while(Size(s)):
        rem=Pop(s)
        print(rem.val,end=' ')

        if rem.right:
            Push(s,rem.right)
        if rem.left:
            Push(s,rem.left)

def preorderRecursive(node):
    if node:
        print(node.val,end=' ')
        preorderRecursive(node.left)
        preorderRecursive(node.right)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
preorderRecursive(root)
print()
preorder(root)