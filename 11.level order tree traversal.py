class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Queue():
    queue=[]
    return queue
def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def levelorder(node):

    queue=Queue()
    Enqueue(queue,node)

    while(Size(queue)):
        rem=Dequeue(queue)
        print(rem.val,end=' ')

        if rem.left:
            Enqueue(queue,rem.left)
        if rem.right:
            Enqueue(queue,rem.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
levelorder(root)
