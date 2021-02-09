class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

def storesum(node,arr):
    if node:
        storesum(node.left,arr)
        arr.append(node.val)
        storesum(node.right,arr)
def replace(node,arr,i):
    if node:
        replace(node.left,arr,i)
        node.val=arr[i[0]-1]+arr[i[0]+1]
        i[0]+=1
        replace(node.right,arr,i)

def replacesum(node):
    inorder(node)
    print()
    arr=[]
    arr.append(0)
    storesum(node,arr)
    arr.append(0)
    i=[1]
    replace(node,arr,i)
    inorder(node)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  
root.right.left = Node(6)
root.right.right = Node(7)

replacesum(root)
