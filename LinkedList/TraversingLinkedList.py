# Linked list is created by using node class
# Create a node object and create another class to this ODE Object
# This linked list is created with three data elements

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class SLinkedList:
    def __init__(self):
        self.headval = None
    
    # create a new method that will print out list
    def listprint(self):
        
        # look at the head of the list 
        printval = self.headval
        
        # head is not none, print and go to next in list
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link the first node to second node (e2)
list.headval.nextval = e2
e2.nextval = e3

# print the linked list
list.listprint()