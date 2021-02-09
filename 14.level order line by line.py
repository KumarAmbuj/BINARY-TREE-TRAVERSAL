class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Queue():
    queue=[]
    return queue

def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def levelorderlinebyline(node):
    queue=Queue()
    Enqueue(queue,node)
    Enqueue(queue,None)

    while(Size(queue)>1):
        rem=Dequeue(queue)

        if rem==None:
            print()
            Enqueue(queue,None)

        else:
            print(rem.val,end=' ')

            if rem.left:
               Enqueue(queue,rem.left)
            if rem.right:
               Enqueue(queue,rem.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
levelorderlinebyline(root)

