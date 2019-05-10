#Luis Renteria
#Dr. Fuentes
#CS 2302 Mon/Wed 1:30 - 2:50

import random
import numpy as np
import math
from mpmath import *


def Identities(Func,tries = 10, tolerance = 0.0001):
    #This method compares every function in the list to ever other function (excluding itself) using a double for loop
    for i in range(len(Func)):
        for j in range(len(Func)):
            #Checking for comparisons against the same function.
            if i != j:
                count = 0
                for x in range(tries):
                    #Evaluating the expressions and comparing the answers.
                    t = random.uniform(-math.pi,math.pi)
                    y1 = eval(Func[i])
                    y2 = eval(Func[j])
                    if np.abs(y1-y2)<tolerance:
                        count = count + 1
                #If the answers matched every time, then the two are equivalent
                if count == tries:    
                    print(Func[i],' is equivalent to ',Func[j])
                    
def PartitionSet(L,n):
    #Checking if the set can be partitioned
    total = 0
    for i in range(len(L)):
        total = total + L[i]
    #If the sum is odd, set cannot be partitioned
    if total%2 == 1:
        print('No partition exist for this set.')
        return
    else:
        #The sum is even, set may be able to be partitioned
        return CalculatePartition(L,n,total//2)

def CalculatePartition(L,n,total):
    #Incomplete
    if total == 0:
        return True,[]
    if n == 0 and total != 0:
        return False,[]
    if L[n-1] > total:
        #If the last element is greater than half the sum of the set, a partition does not exist.
        return False
    ans,sub = CalculatePartition(L,n-1,total-L[n-1])
    if ans == True:
        sub.append(L[n-1])
        return True,sub
    
            
                    
                    
#Here we initialize a list of all functions that are to be tested.                    
Func = ['' for x in range(16)]

Func[0] = 'sin(t)'
Func[1] = 'cos(t)'
Func[2] = 'tan(t)'
Func[3] = 'sec(t)'
Func[4] = '-sin(t)'
Func[5] = '-cos(t)'
Func[6] = '-tan(t)'
Func[7] = 'sin(-t)'
Func[8] = 'cos(-t)'
Func[9] = 'tan(-t)'
Func[10] = 'sin(t)/cos(t)'
Func[11] = '2*sin(t/2)*cos(t/2)'
Func[12] = 'sin(t)*sin(t)'
Func[13] = '1-(cos(t)*cos(t))'
Func[14] = '(1-cos(2*t))/2'
Func[15] = '1/cos(t)'

Identities(Func)

Set=[2,4,5,9,12]
#print(PartitionSet(Set,len(Set)))





