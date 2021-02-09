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



def inorderprint(node):
    if node:
        inorderprint(node.left)
        print(node.val,end=' ')
        if node.next:
            print(node.next.val)
        else:
            print(-1)

        inorderprint(node.right)
def inorder(node):
    temp=node
    while(temp.left):
        temp=temp.left

    while(temp):
        print(temp.val)
        temp=temp.next


root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(3)


inordersuccessor(root)

inorderprint(root)
inorder(root)




