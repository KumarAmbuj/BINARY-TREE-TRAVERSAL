class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def MorrisTraversal(root):
    curr = root

    while curr:

        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right

        else:

            prev = curr.left

            while prev.right is not None and prev.right is not curr:
                prev = prev.right


            if prev.right is curr:
                prev.right = None
                curr = curr.right


            else:
                print(curr.data, end=" ")
                prev.right = curr
                curr = curr.left



def preorfer(root):
    if root:
        print(root.data, end=" ")
        preorfer(root.left)
        preorfer(root.right)




root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)

root.left.right.left = Node(10)
root.left.right.right = Node(11)

MorrisTraversal(root)
print()
preorfer(root)