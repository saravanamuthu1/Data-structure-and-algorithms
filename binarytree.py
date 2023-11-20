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
    def bore(self):
        """
         pointer information
        """
        print(f"{self.right} is right pointer and {self.left} is the left pointer")
class BinarySearchTree():
    """
        creates binary search tree
    """
    def __init__(self):
        """
            initialise a binary search tree
        """
        self.root=None
    def __str__(self):
        """
        dummuy class
        """
        return self.__class__.__name__
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
    def contians(self,node,target):
        """
         checks whether a value is present in the tree
        """
        current_node= node
        while current_node is not None:
            if current_node.value < target:
                curenet_node = current_node.left
            elif current_node.value > target:
                current_node = current_node.right
            else:
                if current_node.value == target:
                    print("value is found")
                    return 0
        else:
            print("the value is not in the binary tree")
            return 0
    def print_inorder(self, node):
        """
            print the bianrysearchtree
        """
        if node is not None:
            self.print_inorder(node.left)
            print(node.value)
            self.print_inorder(node.right)
    def fake_print(self):
        return "thus is fake"
    def fake_print(self):
        return "thus is fake"
if __name__=="__main__":
    testTree = BinarySearchTree()
    testTree.insert_tree(testTree.root, 200)
    testTree.insert_tree(testTree.root, 300)
    testTree.insert_tree(testTree.root, 100)
    testTree.insert_tree(testTree.root, 30)
    testTree.print_inorder(testTree.root)
    testTree.contians(testTree.root, 30)
