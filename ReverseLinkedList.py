import math

def ReverseLinkedList(head):
    
    # assigned to spot before head
    previous = None
    current = head
    
    while True:
        
        # assigns to next value 
        temp = current.next
        
        # points to the next LL which would be "None" before a
        current.next = previous
        
        # pointer moves to current head "a" for restart of cycle
        previous = current
        
        # if the next thing is empty, that means temp is empty. Break
        if not temp:
            break
        
        # temp becomes the new current  
        current = temp
        
    return previous

# input:  a -> b -> c -> d -> none
# return: None <- a <- b <- c <- d