#Luis Renteria
#CS 2302
#Olac Fuentes, M/W 1:30-2:50
# Code to implement a B-tree 
# Programmed by Olac Fuentes
# Last modified February 28, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def ComputeHeight(T):
    #This method computes the height of the tree.
    if T.isLeaf:
        return 0
    else:
        return 1 + ComputeHeight(T.child[0])
    
def TreeToList(T,L):
    #This method computes akes the items in a b-tree and puts them into a sorted list.
    if T.child[0].isLeaf or T.child[-1].isLeaf:
        #this statement checks to see if the children are leaves, if so, the list building begins.
        for i in range(len(T.item)):
            #This for loop goes through each child of a node, concatenateing it to the list, then concatenating
            #a part of the parent one part at a time.
            L += T.child[i].item
            L.append(T.item[i])
        #After the for loop, the last child is added, then the list is returned.    
        L += T.child[-1].item    
        return L
    else:
        #until the parents of leaves are found, the method goes through the tree
        TreeToList(T.child[0],L)
        L +=T.item
        TreeToList(T.child[-1],L)
    
        
def MinElement(T,depth):
    #This Method returns the smallest element at a given depth
    if depth < 0:
        print("Please choose a positive number.")
        return None
    if depth == 0:
        return T.item[0]
    else:
        return MinElement(T.child[0], depth-1)

def MaxElement(T,depth):
    #This method returns the largest element at a given depth
    if depth < 0:
        print("Please choose a positive number.")
        return None
    if depth == 0:
        return T.item[-1]
    else:
        return MaxElement(T.child[-1], depth-1)
    
def NodesAtDepth(T,depth):
    #This method returns the number of nodes at a given depth
    if depth < 0:
        print('Please choose a positive integer')
        return None
    if depth == 1 and T.isLeaf:
        print('There are no nodes at this depth.')
        return None
    if depth == 1:
        #once the parents of the nodes are found, the method returns the number of children.
        return len(T.child)
    else:
        return NodesAtDepth(T.child[0], depth-1) + NodesAtDepth(T.child[-1], depth-1)
    
def PrintAtDepth(T,depth):
    #This method prints all elements at the specified depth
    if depth < 0:
        print('Please choose a positive number')
        return None
    if depth == 0:
        print(T.item)
        return
    if depth == 1 and T.isLeaf:
        print('There are no elements at that depth.')
        return 
    if depth == 1:
        #once the parents of the specified nodes are found, the method prints out each child's elements.
        for i in range(len(T.item)+1):
            print(T.child[i].item)
        return
    else:
        PrintAtDepth(T.child[0],depth-1)
        PrintAtDepth(T.child[-1],depth-1)
        
def FullNodes(T,count):
    #This method returns the number of nodes that are full within the b-tree
    if len(T.item) == 5:
        count+=1
    if T.isLeaf:
        return count
    else:
        #this loop iterates through the child of every parent until a leaf is reached.
        for i in range(len(T.item)+1):
            count = FullNodes(T.child[i],count)
    return count

def FullLeaves(T,count):
    if T.isLeaf:
        #If a node is a leaf, the number of elements is checked.
        if len(T.item) == 5:
            count+=1
        return count
    else:
        #this for loop iterates until the leaves are reached
        for i in range(len(T.item)+1):
            count = FullLeaves(T.child[i],count)
    return count

def FindKeyDepth(T, k, d):
    #This method returns the depth that a specified key is located in.
    if k in T.item:
        return d
    elif T.isLeaf:
        #if the key has not yet been located, and the current node is a leaf, -1 is returned.
        return -1
    else:
        #the FindChild method is used to determine which node should be searched next, given the key.
        return FindKeyDepth(T.child[FindChild(T,k)],k,d+1)
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    #print('Inserting',i)
    Insert(T,i)
    #PrintD(T,'') 
    #Print(T)

PrintD(T,'')   
print('At what depth would you like the largest item to be located?')
depth = int(input())
print('The maximum element at depth ', depth , 'is: ') 
print(MaxElement(T, depth))
print('############################################################')

print('At what depth would you like the smallest item to be located?')
depth = int(input())
print('The minimum element at depth ', depth , 'is: ') 
print(MinElement(T, depth))
print('############################################################')

print('At what depth do you want to know the number of nodes?')
depth = int(input())
print('At depth ',depth, ', the number of nodes is: ')
print(NodesAtDepth(T, depth))
print('############################################################')

print('At what depth would like all the items printed?')
depth = int(input())
print('At depth ',depth, ' , the items are: ')
PrintAtDepth(T,depth)
print('############################################################')
     
print('The height of the tree is:')
print(ComputeHeight(T))
print('############################################################')


List = []
TreeToList(T,List)
print('The List of the tree is: ')
print(List)
print('############################################################')

print('The amount of full nodes is: ')
print(FullNodes(T,0))
print('############################################################')

print('The amount of full leaves is: ')
print(FullLeaves(T,0))
print('############################################################')

print('What key would you like to find the depth of?')
key = int(input())  
print('The key ', key, ' is located at depth: ')    
print(FindKeyDepth(T,key,0))







