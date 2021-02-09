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

def spiral(node,l,flag):
    if node==None:
        return

    if l==0:
        print(node.val,end=' ')

    if l<0:
        return
    if flag==False:
        spiral(node.left,l-1,flag)
        spiral(node.right,l-1,flag)
    else:
        spiral(node.right,l-1,flag)
        spiral(node.left,l-1,flag)

def findspiral(node):
    h=height(node)
    flag=False
    x=0
    for i in range(h+1):
        x+=1
        spiral(node,i,flag)
        print()

        if x==2:
            x=0
            flag=~flag


root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
root.right.right = Node(7);
root.left.left.left = Node(8);
root.left.left.right = Node(9);
root.left.right.left = Node(3);
root.left.right.right = Node(1);
root.right.left.left = Node(4);
root.right.left.right = Node(2);
root.right.right.left = Node(7);
root.right.right.right = Node(2);
root.left.right.left.left = Node(16);
root.left.right.left.right = Node(17);
root.right.left.right.left = Node(18);
root.right.right.left.right = Node(19);

findspiral(root)




