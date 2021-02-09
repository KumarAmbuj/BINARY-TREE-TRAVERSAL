class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def height(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 0

    l=height(node.left)
    r=height(node.right)
    return max(l,r)+1
def findspiral(node):
    h=height(node)
    flag=False
    for i in range(h+1):

        spiral(node,i,flag)
        flag=~flag

def spiral(node,l,flag):

    if node==None:
        return
    if l<0:
        return

    if l==0:
        print(node.val,end=' ')
        return

    if flag==False:
        spiral(node.right,l-1,flag)
        spiral(node.left, l - 1, flag)
    else:
        spiral(node.left, l - 1, flag)
        spiral(node.right, l - 1, flag)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
findspiral(root)
print()
inorder(root)