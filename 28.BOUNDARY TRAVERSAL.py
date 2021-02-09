class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printleft(node):
    if node:

        if node.left:
            print(node.val,end=' ')
            printleft(node.left)

        elif(node.right):
            print(node.val,end=' ')
            printleft(node.right)

def printleaf(node):
    if node==None:
        return
    if node.left==None and node.right==None:
        print(node.val,end=' ')
    printleaf(node.left)

    printleaf(node.right)


def printright(node):

    if node:
        if node.right:
            printright(node.right)
            print(node.val,end=' ')
        elif node.left:
            printright(node.left)
            print(node.val,end=' ')



def printboundary(node):
    print(node.val,end=' ')
    printleft(node.left)

    printleaf(node.left)

    printleaf(node.right)

    printright(node.right)

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printboundary(root)