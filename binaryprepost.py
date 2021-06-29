class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
class NumberofNodesinbinary:
    def __init__(self):
        self.root=None
    def preorder(self,root):
        if root is None:
            return 0
        else:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return 0
        else:
           
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def inorder(self,root):
        if root is None:
            return 0
        else:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
     
    def numNodes(self,root):
        if root is None:
            return 0
        return 1+ self.numNodes(root.left)+ self.numNodes(root.right)
if __name__=='__main__':
    tree=NumberofNodesinbinary()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    print("pre order traversal is:",end=" ")
    tree.preorder(tree.root)
    print()
    print("post order traversal is:",end=" ")
    tree.postorder(tree.root)
    print()
    print("inorder traversal is:",end=" ")
    tree.inorder(tree.root)
    print()
    print("number of nodes",end=" ")
    print(tree.numNodes(tree.root))
    
    
    
        
5
