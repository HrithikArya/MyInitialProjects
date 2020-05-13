#code
times = int(input("Enter round"))
c = []
for i in range(0, times) :
    a = input()
    b = input()
    c.append(a+b)
for i in range(0, times) :
    if c[i] == 'RR' :
        print('DRAW')
    elif c[i] == 'RS' :
        print('A')
    elif c[i] == 'RP' :
        print('DRAW')
    elif c[i] == 'SS' :
        print('DRAW')
    elif c[i] == 'SR' :
        print('B')
    elif c[i] == 'SP' :
        print('A')
    elif c[i] == 'PP' :
        print('DRAW')
    elif c[i] == 'PS' :
        print('B')
    elif c[i] == 'PR' :
        print('A')
    else :
        print("Sorry wrong")
