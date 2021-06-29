class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
class Numberofnonleafnodes:
    def __init__(self):
        self.root=None
    def non(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1+self.non(root.left)+self.non(root.right)
if __name__=='__main__':
    tree=Numberofnonleafnodes()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    print("number of  non nodes",end=" ")
    print(tree.non(tree.root))
