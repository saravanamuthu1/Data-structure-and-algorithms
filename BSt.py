class Node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.value=value
class Binary_search_tree():
    def __init__(self):
        self.root=None
    def insertTree(self,node,value):
        if self.root is None:
            self.root=Node(value)
        else:
            if node.value < value:
                if node.left is not None:
                    self.insertTree(node.left,value)
                else:
                    node.left=Node(value)
            elif node.value > value:
                if node.right is not None:
                    self.insertTree(node.right,value)
                else:
                    node.right = Node(value)
            else:
                print('the value is already present in the node')
    def printInorder(self, node):
        if node!=None:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)
if __name__=="__main__":
    testTree = Binary_search_tree()
    testTree.insertTree(testTree.root, 200)
    testTree.insertTree(testTree.root, 300)
    testTree.insertTree(testTree.root, 100)
    testTree.insertTree(testTree.root, 30)
    testTree.printInorder(testTree.root)
    