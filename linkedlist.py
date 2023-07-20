"""
    create,update,delete,reverse,get index,print
"""
class Node:
    """ 
    create node class wiht data and pointer 
    """
    def __init__(self,value):
        """
            initialise the constructor 
        """
        self.data=value
        self.next=None
    def __str__(self):
        """
        dummuy class
        """
        return self.__class__.__name__
""" 
Create a linked list
"""
class LinkedList():
    """ 
    Create a linked list
    """
    def __init__(self) -> None:
        """
            initialise the constructor for linkedlist
        """
        self.head=None
    def __str__(self):
        """
        dummuy class
        """
        return self.__class__.__name__
    def insert_value(self,value):
        """ 
        insert the value in linked list
        """
        current_node=Node(value)
        if self.head is None:
            self.head=current_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=current_node
    def delete_value(self,target_value):
        """ 
        Delete a certain value from the linked list
        """
        current_node=self.head
        prev_node=None
        if current_node.data == target_value:
            self.head=current_node.next
            print("first node is deleted")
            return 0
        while current_node is not None:
            if current_node.data==target_value:
                if current_node.next is None:
                    prev_node.next=None
                    print('last node is deleted')
                    return 0
                print('middle node is deleted')
                prev_node.next=current_node.next
                return 0
            prev_node=current_node
            current_node=current_node.next
    def get_index(self,target_value):
        """ 
        Get the index of the certain element 
        """
        current_node =self.head
        count=0
        while current_node is not None:
            if current_node.data == target_value:
                print("the index of the target value is"+" "+str((count+1)))
                return 
            current_node = current_node.next
            count+=1
    def reverse_list(self):
        """ 
        Reverse the given linked list
        """
        prev_node=None
        current_node=self.head
        while current_node is not None:
            next_node=current_node.next
            current_node.next =prev_node
            prev_node=current_node
            current_node=next_node
        self.head=prev_node
    def print_list(self):
        """
        print the linked list 
        """
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next
if __name__=="__main__":
    obj1=LinkedList()
    obj1.insert_value(5)
    obj1.insert_value(6)
    obj1.insert_value(7)
    obj1.insert_value(9)
    obj1.reverse_list()
    obj1.get_index(7)
    obj1.print_list()
    