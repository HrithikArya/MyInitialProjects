t = int(input('''It's a short script in which you have to provide a list and
a number and this script search through the list if it can find the countDown
from the provides number like if you inserted 4 this will search for 4,3,2,1 .  
Enter testcases: '''))
for i in range(t) :
    length, num = map(int, input('Enter length of list and number from which you want to countdown seperated by space: ').split())
    list1 = list(map(int, input('Enter list elements seperated by space: ').split()))
    c = 0
    print("Searching in list...")
    for k in range(len(list1)) :
        if list1[k] == num:
            try :
                if list1[k+num-1] == num-num+1 :
                    c += 1
            except :
                c = c
    print('Case #',i+1,': total Number of countDown found',c)
    
