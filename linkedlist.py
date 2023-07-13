""" create node class wiht data and pointer """
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
""" Create a linked list"""
class LinkedList():
    def __init__(self) -> None:
        self.head=None
    """ insert the value in linked list"""
    def insertValue(self,value):
        currentNode=Node(value)
        if self.head is None:
            self.head=currentNode
        else:
            temp=self.head
            while temp.next!= None:
                temp=temp.next
            temp.next=currentNode
    """ Delete a certain value from the linked list"""
    def deleteValue(self,targetValue):
        currentNode=self.head
        prevNode=None
        if currentNode.data == targetValue:
            self.head=currentNode.next
            print("first node is deleted")
            return 0
        else:
            while currentNode is not None:
                if currentNode.data==targetValue:
                    if currentNode.next is None:
                        prevNode.next=None
                        print('last node is deleted')
                        return 
                    else:
                        print('middle node is deleted')
                        prevNode.next=currentNode.next
                        return 0
                else:
                    prevNode=currentNode
                    currentNode=currentNode.next
    """ Get the index of the certain element """
    def getIndex(self,targetValue):
        currentNode =self.head
        count=0
        while currentNode is not None:
            if currentNode.data == targetValue:
                print("the index of the target value is"+" "+str((count+1)))
                return 
            else:
                currentNode = currentNode.next
                count+=1
    """ Reverse the given linked list"""
    def reverseList(self):
        prevNode=None
        currentNode=self.head
        while currentNode is not None:
            nextNode=currentNode.next
            currentNode.next =prevNode
            prevNode=currentNode
            currentNode=nextNode
        self.head=prevNode
    """ print the linked list """
    def printList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next
if __name__=="__main__":
    obj1=LinkedList()
    obj1.insertValue(5)
    obj1.insertValue(6)
    obj1.insertValue(7)
    obj1.insertValue(9)
    obj1.reverseList()
    obj1.getIndex(7)
    obj1.printList()