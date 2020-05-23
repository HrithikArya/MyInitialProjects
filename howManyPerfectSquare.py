import math
def isPerfectSquare(x): 
  
    # Find floating point value of  
    # square root of x. 
    sr = math.sqrt(x) 
   
    # If square root is an integer 
    return ((sr - math.floor(sr)) == 0)

t= int(input())
for a in range(t) :
    l = int(input())
    list1 = list(map(int,input().split()))
    c = 0
    for i in range(l) :
##        if i == l-1 :
##            if (isPerfectSquare(list1[i])):
##                c = c + 1
        for j in range(i+1,l+1) :
            if (isPerfectSquare(sum(list1[i:j]))):
                #print(sum(list1[i:j]),list1[i])
                #print(c)
                c = c + 1
    print(c)
