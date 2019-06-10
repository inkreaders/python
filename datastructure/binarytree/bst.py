class Node(object):
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.__insertNode(data, self.root)
    
    def __insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.__insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.__insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            self.getMin(node.leftChild)
        else:
            return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self, node):
        if node.rightChild:
            self.getMax(node.rightChild)
        else:
            return node.rightChild

    def traverse(self, node):
        if self.root:
            self.traverseInOrder(node)

    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s " % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self, data):
        if self.root:
            self.__removeNode(self.root, data)

    def __removeNode(self, node, data):
        #Case 1: Node to be deleted is leaf node as left child
        #Case 1: Node to be deleted is leaf node as right child
        #Case 3: Node to be deleted is root node
        #Case 3.1: Node to be deleted having left child
        #Case 3.2 Node to be deleted having right child
        #Case 3.3 Node to be deleted having both child   
        print()


bst = BinarySearchTree()

bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)
bst.insert(30)

bst.traverse(bst.root)


        


