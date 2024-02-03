import math
import array as arr

def ex ():
    print ("A: ")
    a = int(input())

    print ("Result: ", math.tan(3*a))

def ex1 ():
    print ("X: ")
    x = int(input())

    print ("N: ")
    n = int(input())

    while(n>1):
         x*=x
         n-=1
    if(n==0):
         x=1

    print ("\nX: ", x)


def ex2 ():
    
    a = [[1,2,3],[-1,5,6],[0,8,9]]
    print ("A: ", a)
    b = [[-1,2,3],[1,5,-6],[0,-8,9]]
    print ("B: ", b)
    
    r = int(input("Number of rows:"))
    co = int(input("Number of columns:"))

    c =[]
    
    print("Input array: ")

    
    #c = [[int(input()) for x in range (co)] for y in range(r)]

    for i in range(r): 
         d=[]  
         for j in range(co): 
             el = int(input())
             d.append(el)
         c.append(d)

    print ("C: ", c) 



    k=0
    
    for j in range(len(a)):
        for i in range(len(a)):
          #  print (a[i][j])
            if(a[i][j] < 0):
                 k+=1
                 break


    print ("\nA: ")
    if((len(a)-k)>0):
         print ("Yes: ",(len(a)-k),"\n")
         k=0
    else: 
         print ("No\n")
         k=0

    
    for j in range(len(b)):
        for i in range(len(b)):
          #  print (b[i][j])
            if(b[i][j] < 0):
                 k+=1
                 break

    print ("\nB: ")
    if((len(b)-k)>0):
         print ("Yes: ",(len(b)-k),"\n")
         k=0
    else: 
        print ("No\n") 
        k=0


    for j in range(co):
        for i in range(r):
          #  print (c[i][j])
            if(c[i][j] < 0):
                 k+=1
                 break

    print ("\nC: ")
    if((co-k)>0):
         print ("Yes: ",(co-k),"\n")
         k=0
    else: 
         print ("No\n")
         k=0


    

print ("N: ")
n = int(input())

match n:
        case 1:
            ex()
        case 2:
            ex1()
        case 3:
            ex2()
        case default:
            print ("Error")