'''You are given all numbers between 1,2,…,n except one. Your task is to
find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
2≤n≤2⋅105
Example

Input:
5
2 3 1 5

Output: 4
'''
l = int(input("Enter n: "))

try :
    a = list(map(int, input('Enter: ').split()))
except :
    print('Wrong input')

a.sort()

for i in range(0,l) :
    if a[i] == i+1 :
        continue
    else :
        print(i+1)
        break
