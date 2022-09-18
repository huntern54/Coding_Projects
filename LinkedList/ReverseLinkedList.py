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
    
    # Insert a new node at beginning
    def InsertAtBeginning(self, newData):
        NewNode = Node(newData)
    
        # Update new nodes next value to existing nodes
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def InsertAtEnd(self, newData):
        NewNode = Node(newData)
        
        # check if the head of the list is empty, if it is, put at the beginning
        if self.headval is None:
            self.headval = NewNode
            return
        # assign the last node as the head
        lastNode = self.headval
        
        # have the last node point to a new empty node
        # last node becomes second the last and the new last is assigned
        while lastNode.nextval:
            lastNode = lastNode.nextval
        lastNode.nextval = NewNode
        
    def InsertInBetween(self, middleNode, newData):
        # check to see if there are more than 2 or more things in list
        if middleNode is None:
            print("There is no middle node")
            return
        
        # Initalize a new node
        NewNode = Node(newData)
        
        # New Nodes next vale will be the middle
        NewNode.nextval = middleNode.nextval
        
        # Middle is where inserted
        middleNode.nextval = NewNode
        
    def ReverseLinkedList(self):
    
        # assigned to spot before head
        previous = None
        current = self.headval
        
        while True:
            
            # assigns to next value 
            temp = current.nextval
            
            # points to the next LL which would be "None" before a
            current.nextval = previous
            
            # pointer moves to current head "a" for restart of cycle
            previous = current
            
            # if the next thing is empty, that means temp is empty. Break
            if not temp:
                break
            
            # temp becomes the new current  
            current = temp
            
        return previous
        
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thur")

# Link the first node to second node (e2)
list.headval.nextval = e2
e2.nextval = e3

# Insert 
list.InsertAtBeginning("Sun")
list.InsertAtEnd("Fri")

# looks at this node "e2" and put between e2 and e3 (in a way, it just puts after e2)
list.InsertInBetween(e2, "Wed")

#Reverse the new list
list.ReverseLinkedList()

list.listprint()

# input:  a -> b -> c -> d -> none
# return: None <- a <- b <- c <- d