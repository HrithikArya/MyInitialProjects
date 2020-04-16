great = None
small = None

while True :
    i = input('Enter response: ')
    if i == 'done' :
        break
    if great == None :
        great = int(i)
    elif int(i) > great :
        great = int(i)
    elif int(i) < great :
        if small == None :
            small = int(i)
        elif int(i) < small :
            small = int(i)


print('great', great)
print('small', small)
        
