class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def inorder(node):
    if node:
        print(node.val, end=' ')
        inorder(node.left)

        inorder(node.right)

def makeTree(arr,s,end):
    trees = []


    if s > end:
        trees.append(None)
        return trees


    for i in range(s, end + 1):


        ltrees = makeTree(arr, s, i - 1)


        rtrees = makeTree(arr, i + 1, end)


        for j in ltrees:
            for k in rtrees:

                node = Node(arr[i])


                node.left = j


                node.right = k


                trees.append(node)
    return trees


arr=[1,2,3,4,5]
l=makeTree(arr,0,len(arr)-1)
for i in l:
    inorder(i)
    print()

