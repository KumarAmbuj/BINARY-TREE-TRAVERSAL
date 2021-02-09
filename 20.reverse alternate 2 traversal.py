class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorderstore(node,l,s):
    if node:
        inorderstore(node.left,l+1,s)
        if l%2==1:
            s.append(node.val)
        inorderstore(node.right,l+1,s)

def inorderreplace(node,l,s,c):
    if node:
        inorderreplace(node.left,l+1,s,c)
        if l%2==1:
            node.val=s[c[0]]
            c[0]+=1
        inorderreplace(node.right,l+1,s,c)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)

def replace(node):
    inorder(node)
    print()
    s=[]
    inorderstore(node,0,s)
    c=[0]
    s=s[::-1]
    inorderreplace(node,0,s,c)
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
replace(root)

