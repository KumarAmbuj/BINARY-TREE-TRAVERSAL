class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)

def spiral(node):
    s1=Stack()
    s2=Stack()
    Push(s1,node)

    while(Size(s1)>0 or Size(s2)>0):

        while(Size(s1)>0):

            rem=Pop(s1)
            print(rem.val,end=' ')

            if rem.right:
                Push(s2,rem.right)
            if rem.left:
                Push(s2,rem.left)

        while(Size(s2)>0):

            rem=Pop(s2)
            print(rem.val,end=' ')

            if rem.left:
                Push(s1,rem.left)
            if rem.right:
                Push(s1,rem.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
spiral(root)
