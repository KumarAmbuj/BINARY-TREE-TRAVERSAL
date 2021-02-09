class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None

arr=[None]
def inordersuccessor(node):
    if node:
        inordersuccessor(node.right)
        node.next=arr[0]
        arr[0]=node
        inordersuccessor(node.left)

def inorder(node,node1):
    if node:
        inorder(node.left,node1)
        if node==node1:
            if node.next:
                print(node.next.val)
            else:
                print('not possible')
        inorder(node.right,node1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
inordersuccessor(root)

inorder(root,root.right)
inorder(root, root.left.left)

