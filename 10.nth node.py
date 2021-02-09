class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def inorder(node,n,count):
    if node:
        inorder(node.left,n,count)
        count[0]+=1
        if count[0]==n:
            print(node.val)
        inorder(node.right,n,count)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

count=[0]
inorder(root,4,count)
