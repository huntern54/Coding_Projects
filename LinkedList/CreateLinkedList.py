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

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link the first node to second node (e2)
list1.headval.nextval = e2
e2.nextval = e3
