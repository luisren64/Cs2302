

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

def IterateSearch(T,k):
    temp = T
    while temp is not None:
        if temp.item == k:
            return temp.item
        if temp.item < k:
            temp = temp.right
        else:
            temp = temp.left

def TreeToList(T,L):
    #This Method takes a tree and inserts the items into a list in acending order.
    if T.left == None and T.right == None:
        L.append(T.item)
        return
    elif T.left == None and T.right is not None:
        L.append(T.item)
        TreeToList(T.right,L)
    elif T.left is not None and T.right is not None:
        TreeToList(T.left,L)
        L.append(T.item)
        TreeToList(T.right,L)
    elif T.right == None and T.left is not None:
        TreeToList(T.left,L)
        
        
def PrintByDepth(T, depth):
    if T == None:
        return
    if depth == 0 :
        print('Keys at depth ',depth,': ',end = ' ')
        print(T.item, end = ' ')
        print()
    print('Keys at depth ',depth + 1,': ',end = ' ')
    if T.left is not None:
        print(T.left.item, end = ' ')
    if T.right is not None:
        print(T.right.item, end = ' ')
    print()
    PrintByDepth(T.left, depth+1)
    PrintByDepth(T.right, depth+1)
    
def ListToTree(T,L):
    temp1 = T
    temp2 = T
    mid1 = (len(L)//2 + len(L))//2
    mid2 = (len(L)//2)//2
    T.item = L[len(L)//2]#Establishing the root at the middle of the list for balance
    T.left.item = L[mid1]#Estalishing the first left branch
    T.right.item = L[mid2]#Establishing the first right branch
    temp1 = T.left
    temp2 = T.right
    i = 0
    while i <= len(L):    
        temp1.left.item = L[mid1]
        temp1.right.item = L[mid1]
        temp2.left.item = L[mid2]
        temp2.left.item = L[mid2]
    
# Code to test the functions above
T = None
T2 = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
B = [10, 4, 15, 18, 12, 2, 8, 1, 3, 5, 9, 7]
for b in B:
    T2 = Insert(T2, b)
C = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 15, 18] 
#InOrder(T)
#print()
#InOrderD(T,'')
#print()
ListTree = None
#print(IterateSearch(T,15))
List = []
TreeToList(T,List)
print(List)
PrintByDepth(T2,0)
print()
InOrderD(T2,' ')
ListToTree(ListTree, C)
#InOrderD(ListTree)
