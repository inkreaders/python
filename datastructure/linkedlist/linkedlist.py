class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def getHeadNode(self):
        if self.head is not None:
            print("{} {}".format("Head node in list: ", self.head.data))
        else:
            print("List is empty.")    

    def traverseList(self):
        tempHeadNode = self.head
        while tempHeadNode is not None:
            print(tempHeadNode.data)
            tempHeadNode = tempHeadNode.nextNode

    def findNodeinList(self, data):
        tempNode = self.head
        while tempNode is not None:
            if tempNode.data == data:
                print("{} {}".format("Node found: ", tempNode.data))
                break
            else:
                tempNode = tempNode.nextNode     
        else:
            print("Node not found.")     

    def removeNodeFromList(self):
        print()

# Operations on list
linkedList = LinkedList()
linkedList.getHeadNode()
linkedList.addNode(1)
linkedList.addNode(2)
linkedList.addNode(3)
linkedList.addNode(4)
linkedList.getHeadNode()
linkedList.traverseList()
linkedList.findNodeinList(7)