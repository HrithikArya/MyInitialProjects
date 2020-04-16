a = int(input("Enter times: "))
print(a)
b = []
for i in range(0, a) :
    k = int(input('Enter num : '))
    b.append(k)
print(b)
def pair() :
    for q in range(0,len(b)-1) :
        for w in range(q + 1,len(b)) :
            if b[q] == b[w] :
                b.pop(w)
                b.pop(q)
if a % 2 == 0 :
    for i in range(0, a / 2) :
        pair()
else :
    for i in range(0, int((a + 1) / 2)) :
        pair()
print(b)
print('Pair', (a - len(b)) / 2)

            
            
