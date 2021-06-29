class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
class Numberofleafnodes:
    def __init__(self):
        self.root=None
    def leafnode(self,root):
        if root is None:
            return 0
    
        if root.left is None and root.right is None:
            return 1
        return self.leafnode(root.left)+ self.leafnode(root.right)
    def notleafnode(self,root):
        if root is None:
            return 0
        if root.left is not None or root.right is not None:
            return 1
        return 1+self.notleafnode(root.left)+self.notleafnode(root.right)
if __name__=='__main__':
    tree=Numberofleafnodes()
    tree.root=Node(1)
    tree.root.left= Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)

    print("leaf node is:",end=" ")
    print(tree.leafnode(tree.root))
   # print("nnonnnleaf node is:",end=" ")
    #print(tree.notleafnode(tree.root))
