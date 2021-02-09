class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def diagonal(node,hash,l):

    if node==None:
        return

    if l in hash:
        hash[l].append(node.val)
    else:
        hash[l]=[]
        hash[l].append(node.val)

    diagonal(node.left,hash,l-1)
    diagonal(node.right,hash,l)

def finddiagonal(node):
    hash={}
    diagonal(node,hash,0)

    for x in hash:
        print(hash[x])

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

finddiagonal(root)

