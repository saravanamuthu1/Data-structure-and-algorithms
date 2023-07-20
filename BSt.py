"""
    create a binary search tree
"""
class Node: 
    """
        creates a class with left,right,value
    """
    def __init__(self,value):
        """
            initalise a constructor for binary search tree
        """
        self.right=None
        self.left=None
        self.value=value
    def __str__(self):
        """
        dummuy class
        """
        return self.__class__.__name__
class BinarySearchTree():
    """
        creates binary search tree
    """
    def __init__(self):
        """
            initialise a binary search tree
        """
        self.root=None
    def insert_tree(self,node,value):
        """
            insert values into the binary search tree
        """
        if self.root is None:
            self.root=Node(value)
        else:
            if node.value < value:
                if node.left is not None:
                    self.insert_tree(node.left,value)
                else:
                    node.left=Node(value)
            elif node.value > value:
                if node.right is not None:
                    self.insert_tree(node.right,value)
                else:
                    node.right = Node(value)
            else:
                print('the value is already present in the node')
    def print_inorder(self, node):
        """
            print the bianry search tree
        """
        if node is not None:
            self.print_inorder(node.left)
            print(node.value)
            self.print_inorder(node.right)
if __name__=="__main__":
    testTree = BinarySearchTree()
    testTree.insert_tree(testTree.root, 200)
    testTree.insert_tree(testTree.root, 300)
    testTree.insert_tree(testTree.root, 100)
    testTree.insert_tree(testTree.root, 30)
    testTree.print_inorder(testTree.root)
    