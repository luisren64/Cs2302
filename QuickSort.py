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
    curr1 = L1.head
    curr2 = L2.head
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
        while curr1 is not None and curr2 is not None:
            if curr1.item <= curr2.item:
                Append(Merged,curr1.item)
                curr1 = curr1.next
            else:
                Append(Merged,curr2.item)
                curr2 = curr2.next
    while curr2 is not None:
        Append(Merged,curr2.item)
        curr2 = curr2.next
    
    while curr1 is not None:
        Append(Merged,curr1.item)
        curr1 = curr1.next
    
    return Merged
            
            

def QuickSort(L):
    if IsEmpty(L):
        return None
    if L.head.next == None:
        return L
    else:
        smaller = List() #This wil handle the items smaller than the pivot
        larger = List() #This will handle the items greater than the pivot
        
        i = 0
        pivot = L.head
        curr = L.head
        #Here I append based on the pivot, with smaller or larger
        while curr is not None:
            if curr.item < pivot.item:
                Append(smaller,curr.item)
            if curr.item > pivot.item:
                Append(larger,curr.item)
            curr = curr.next
            i = i + 1
        #After all has been appended, I append the pivot to the larger list if
        #it contains no elements. If it does, then I append to the smaller list.
        if larger.head == None:
            Append(larger, pivot.item)
        else:
            Append(smaller, pivot.item)
        
        smaller = QuickSort(smaller)
        larger = QuickSort(larger)
        
        
        L = Merge(smaller,larger)
                
        #Print(Merged)
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
    location = length//2
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
    ListCopy = QuickSort(ListCopy)
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

