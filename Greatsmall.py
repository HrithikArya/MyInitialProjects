num = []
while True :
    i = input('Enter num: ')
    if i == 'done' :
        break
    num.append(int(i))
print(num)
a = 0    
for k in range(a, len(num)-1) :
        if num[k] > num[0] :
            num[k], num[0] = num[0], num[k]
            print(num)


