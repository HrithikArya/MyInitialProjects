i = int(input('Enter times: '))
list = []

def MidNumber() :
    for a in range(0, i) :
        a = int(input('Enter the count: '))
        for b in range(0, a):
            b = int(input('Enter list elements: '))
            list.append(b)
        
        print(list)
        n = len(list)
        if (n % 2 == 0):
            m = n / 2 + 1
            print(list[int((n/2))])
        else :
             print(list[int((n+1/2)-1)])
        list.clear()

MidNumber()
print('Want to repeat??')
print('Yes OR No')
ans = input('Enter Response: ')

if ans == 'yes' :
    MidNumber()
elif ans == 'no' :
    print('OK Thanks')
else :
    print('Sorry!! I don\'t understand')
