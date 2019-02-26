import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
            

def BuildList(new,n):
    #This method recieves an integer of the user's choosing and builds
    # a list of random integers of that length
    if n == 0:
        return None
    else:
        for i in range(0,n):
          Append(new,random.randint(0,101))
        
        return new  
            

def BubbleSort(L):
    #This method sorts a list by swapping adjacent elements and putting them
    #in ascending order.
    if IsEmpty(L):
        return None
    
    curr = L.head
    while curr.next is not None:
        if curr.item > curr.next.item:
            #temp is used to store to current node's item before swapping
            temp = curr.item
            curr.item = curr.next.item
            curr.next.item = temp
            #If a swap occurs, curr is sent back to the head so that the 
            #list can be checked again to ensure that it is in the correct order.
            curr = L.head
        else:
            curr = curr.next
            
def Copy(L):
    #This method creates a new list 
    #and appends the items of the given list to create a copy
    Copy = List()
    temp =L.head
    while temp is not None:
        Append(Copy,temp.item)
        temp = temp.next
    return Copy

def ElementAt(List, location):
    #This method obtains the median of the list by using the list's length, then
    #returning the item at half the length of the list.
    temp = List.head
    i = 1
    while temp is not None:
        if i == location:
            median = temp.item
        i = i + 1
        temp = temp.next
    return median
            
def Median(L,length):
    #This method returns the median of the List by creating a copy,
    #ordering the copy, then locating the number at half the list's length.
    ListCopy = List()
    ListCopy = Copy(L)
    BubbleSort(ListCopy)
    print('The sorted list is: ')
    Print(ListCopy)
    print('The median of the list is: ')
    median = ElementAt(ListCopy, length//2)
    print(median)    

dataList = List()
print('How long would you like the list to be?')
listLength = int(input())
BuildList(dataList,listLength)
print('The elements in the list are: ')
Print(dataList)
Median(dataList, listLength)


















