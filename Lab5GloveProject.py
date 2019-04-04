#Luis Renteria
#CS 2302
#Olac Fuentes, M/W 1:30-2:50
# Implementation of hash tables with chaining using strings
import numpy as np
import re
import time
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])
            
    def GetNumItems(self):
        return self.num_items
    
    def AddItem(self):
        self.num_items = self.num_items + 1
        
        
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = []
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    #Insert function for the BST
    if T == None:
        T =  BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)

#def SolveByBST():
    #T = None
    #f = open('glove.6B.50d.txt',encoding='utf-8')


        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

def SolveByHash():
    #creating a hash table here
    Table = HashTableC(104729)    
    tStart = time.time()
    f = open('glove.6B.50d.txt',encoding='utf-8')
    print("Building hash table with chaining.")
    #This reads the file line by line and uses the ParseArray method to create the array
    for line in f:
        #The word and its accompanying embedding array are created in ParseArray and inserted
        word, arr = ParseArray(line)
        InsertC(Table,word,arr)
        #The number of items in the table is updated.
        Table.AddItem()
        #here, the table is doubled if the number of items exceeds to length of the table
        if Table.GetNumItems == len(Table.item):
            newSize = (Table.size * 2) + 1
            Table = DoubleTable(Table,newSize)
        
    f.close()
    
    #The hash table creation time is tracked here.
    endTime = time.time() - tStart
    
    SimList = []
    SimList = InsertList(SimList)

    FindSimilaritiesHash(Table, SimList, endTime)    
    
    
def DoubleTable(H,newSize):
    #This method doubles the size of the hash table and re-enters the values
    newTable = HashTableC(newSize)
    for i in H.item:
        for i in range(len(i)):
            InsertC(newTable, i[0], i[1])
   
def ParseArray(line):
    #This method takes a line from the file and returns the word
    #along with the array of embeddings
    fileLine = re.split(" ",line)
    arr = np.empty(50, dtype = float)
    count = 0
    for i in range(0, 50):
        if count == 5:
            break
        if i == 0:
            word = fileLine[i]
        elif i > 0:
            arr[i] = fileLine[i]
        count = count + 1
    return word, arr

def InsertList(L):
    #This method takes the text file of words to compare and inserts the strings into a list of lists
    f = open('WordPairs.txt',encoding = 'utf-8')
    for line in f:
        listLine = re.split(" ",line)
        listLine[-1] = listLine[-1].replace("\n","")
        L.append([listLine[0],listLine[1]])
    return L

def LoadFactor(Table):
    count = 0
    for i in Table.item:
        count = count + len(i)
    return count/len(Table.item)
       
def FindSimilaritiesHash(Table,List,endTime):
    #This method calculates the stats of the has table and the similarities between words.
    print('------------Hash Stats------------')
    print('Initial table size: 104729')
    print('Final table size: ',len(Table.item))
    print('Load Factor: ',LoadFactor(Table))
    print('Table creation time: ',endTime)
    
    for i in range(len(List)):
        print(List[i], end = " ")
        print(((FindC(Table,List[i][0])[1]) * (FindC(Table,List[i][1])[1])) / (abs((FindC(Table,List[i][0])[1])) * abs(FindC(Table,List[i][1])[1]))) 
    
    
    
print("Please choose a table implimentation.")
print("Press 1 for binary search tree, or 2 for hash table with chaining.")
answer = int(input())

if answer == 1:
    print('egg')
elif answer == 2:
    SolveByHash()
else:
    print("Please choose 1 or 2.")
                
        
 

    
    
    