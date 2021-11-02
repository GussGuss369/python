import datetime 
import math

def appendToList(n): 
    alist = [] 
    t0 = datetime.datetime.now()     
    for i in range(n): 
        alist.append(i) 
    t1 = datetime.datetime.now() 
    runtime = (t1 - t0)* 1000  
    print("time to append",n, " items to list ",runtime, "milliseconds") 

def concatenateList(n): 
    alist = [] 
    t0 = datetime.datetime.now()     
    for i in range(n): 
        alist = alist + [i] 
    t1 = datetime.datetime.now() 
    runtime = (t1 - t0)* 1000
    print("time to concatenate ",n, " items to list ",runtime, "milliseconds")                                         

k = int(input ("How many items do you want to add to your list? ")) 
appendToList(k) 
concatenateList(k) 
quit = input() 