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
        self.length = 0
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
    if n == 0:
        return None
    else:
        for i in range(0,n):
          Append(new,random.randint(0,101))
        
        new.length = n
        return new  
            
def Merge(L1,L2):
    Merged = List()
    #Two temporary variables are used to traverse both lists.
    curr1 = L1.head
    curr2 = L2.head
    #This first if statement takes two lists of one element each and merges them.
    if L1.head.next == None and L2.head.next == None :
        if L1.head.item <= L2.head.item:
            Append(Merged,L1.head.item)
            Append(Merged,L2.head.item)
            return Merged
        else:
            Append(Merged,L2.head.item)
            Append(Merged,L1.head.item)
            return Merged
    else:
        #This while loop iterates through both lists simultaneously
        #while comparing items to create anew ordered list.
        while curr1 is not None and curr2 is not None:
            if curr1.item <= curr2.item:
                Append(Merged,curr1.item)
                curr1 = curr1.next
            else:
                Append(Merged,curr2.item)
                curr2 = curr2.next
    #These two while loops append any leftover after one list has been completely
    #iterated through
    while curr2 is not None:
        Append(Merged,curr2.item)
        curr2 = curr2.next
    
    while curr1 is not None:
        Append(Merged,curr1.item)
        curr1 = curr1.next
    
    return Merged
            
            

def MergeSort(L):
    if IsEmpty(L):
        return None
    if L.head.next == None:
        return L
    else:
        L1 = List() #This wil handle the left half
        L2 = List() #This will handle the right half
        
        i = 0
        midpoint = L.length//2
        curr = L.head
        #curr iterates through the list, appending item into the left list (L1)
        #until the midmoint is reached, which is when it will append to the
        #right list (L2)
        while curr is not None:
            if i < midpoint:
                Append(L1,curr.item)
            if i >= midpoint:
                Append(L2,curr.item)
            curr = curr.next
            i = i + 1
        #The lengths of the sublists are set here. this is to determine future midpoints
        L1.length = L.length//2
        L2.length = L.length - L1.length
        #MergeSort is now called recursively until the original list is split into
        #sublists of 1 element
        L1 = MergeSort(L1)
        L2 = MergeSort(L2)
        
        #Merge is now called to begin the process of putting the list back together.
        L = Merge(L1,L2)
                
        
        return L
            
            
        
        
def Copy(L):
    #This method creates a new list 
    #and appends the items of the given list to create a copy
    Copy = List()
    temp =L.head
    while temp is not None:
        Append(Copy,temp.item)
        temp = temp.next
    Copy.length = L.length 
    return Copy

def ElementAt(List, length):
    #This method obtains the median of the list by using the list's length, then
    #returning the item at half the length of the list.
    temp = List.head
    i = 1
    location = length // 2
    while temp is not None:
        if i == location:
            median = temp.item
        i = i + 1
        temp = temp.next
    return median
            
def Median(L):
    #This method returns the median of the List by creating a copy,
    #ordering the copy, then locating the number at half the list's length.
    ListCopy = List()
    ListCopy = Copy(L)
    #Sorted = List()
    ListCopy = MergeSort(ListCopy)
    print('The sorted list is :')
    Print(ListCopy)
    print('The median of the list is: ')
    med = ElementAt(ListCopy, L.length)            
    print(med)
   
dataList = List()
print('How long would you like the list to be?')
listLength = int(input())
BuildList(dataList,listLength)
print('The elements in the list are: ')
Print(dataList)
Median(dataList)



    
    
    
    
    
    
    
    
    
    
    
    