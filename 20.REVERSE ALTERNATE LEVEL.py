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

def levelorderstore(node,l,s):
    if l<0:
        return
    if l==0:
        s.append(node.val)
        return

    levelorderstore(node.left,l-1,s)
    levelorderstore(node.right,l-1,s)


def levelorderreplace(node,l,s,c):
    if l<0:
        return

    if l==0:
        node.val=s[c[0]]
        c[0]+=1

    levelorderreplace(node.left,l-1,s,c)
    levelorderreplace(node.right,l-1,s,c)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)




def reverse(node):
    h=height(node)
    inorder(node)
    print()
    for i in range(1,h+1,2):
        s=[]
        levelorderstore(node,i,s)
        s=s[::-1]
        c=[0]
        levelorderreplace(node,i,s,c)
    inorder(node)

root = Node('a');
root.left = Node('b');
root.right = Node('c');
root.left.left = Node('d');
root.left.right = Node('e');
root.right.left = Node('f');
root.right.right = Node('g'); 
root.left.left.left = Node('h');
root.left.left.right = Node('i');
root.left.right.left = Node('j');
root.left.right.right = Node('k');
root.right.left.left = Node('l');
root.right.left.right = Node('m');
root.right.right.left = Node('n');
root.right.right.right = Node('o');

reverse(root)
