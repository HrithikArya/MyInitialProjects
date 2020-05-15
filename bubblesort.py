a = [8,5,6,3,4,7,1,2]
print(a)
k = int(input("Enter num to search: "))
'''for i in range(1, len(a)) :
    for j in range(1, len(a)) :
        if a[j - 1] > a[j] :
                a[j - 1], a[j] = a[j], a[j - 1]
        print(a)
print(a)
'''

for i in range(1, len(a)) :
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key :
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

print(a)
i = int(len(a)/2)

if k > a[len(a)-1] :
    print('number not found')
        
elif k >= a[i] :
    for j in range(i, len(a)) :
        if k == a[j] :
            print('yes it has ', k, ' on ', j, ' index')
       
elif k < a[i] :
    for j in range(0, i) :
        if k == a[j] :
            print('yes it has ', k, ' on ', j, ' index')

    
