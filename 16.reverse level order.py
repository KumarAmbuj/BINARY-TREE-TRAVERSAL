class Node:


    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def height(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 0
    l=height(node.left)
    r=height(node.right)
    return max(l,r)+1

def findlevel(node,l):

    if l==0:
        print(node.val,end=' ')
    if l<0:
        return

    findlevel(node.left,l-1)
    findlevel(node.right,l-1)


def levelorder(node):
    h=height(node)

    for i in range(h,-1,-1):
        findlevel(node,i)

root = Node(1) 
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

levelorder(root)
