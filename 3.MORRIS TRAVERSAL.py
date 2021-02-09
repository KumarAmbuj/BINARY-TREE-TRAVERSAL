class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def morristraversal(root):
    cur=root

    while(cur):
        if cur.left==None:
            print(cur.val,end=' ')
            cur=cur.right

        else:
            pre=cur.left
            while(pre.right!=None and pre.right!=cur):
                pre=pre.right

            if pre.right==None:
                pre.right=cur
                cur = cur.left

            else:
                print(cur.val,end=' ')
                pre.right=None
                cur=cur.right

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
morristraversal(root)


