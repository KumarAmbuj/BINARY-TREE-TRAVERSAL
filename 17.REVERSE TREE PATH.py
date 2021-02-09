class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def reverse(node,hash,l,x,c):
    if node==None:
        return


    hash[l]=node.val


    if node.val==x:
        node.val=hash[c[0]]
        c[0]+=1
        return True




    if (reverse(node.left,hash,l+1,x,c)):
        node.val=hash[c[0]]
        c[0]+=1
        return True


    if (reverse(node.right,hash,l+1,x,c)):
        node.val=hash[c[0]]
        c[0]+=1
        return True

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


def reversepath(node,x):
    hash={}


    inorder(node)
    print()
    c=[0]
    b=reverse(node,hash,0,x,c)
    if b:
        inorder(node)


root = Node(7);
root.left = Node(6);
root.right = Node(5);
root.left.left = Node(4);
root.left.right = Node(3);
root.right.left = Node(2);
root.right.right = Node(1);

reversepath(root,2)





