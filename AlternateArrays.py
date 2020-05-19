#!user\\
#code
'''Given an unsorted array of positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.

Input:
First line of input contains an integer T denoting the number of test cases. For each testcase, first line contains N, size of array. The subsequent line contains N array elements.

Output:
Print the modified array.
Note: Array should start with positive number.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
-106 ≤ a[] ≤ 107

Example:
Input:
1
9
9 4 -2 -1 5 0 -5 -3 2

Output:
9 -2 4 -1 5 -5 0 -3 2
'''
a = int(input('Enter Testcases: '))

for i in range(0,a) :
    b = int(input('Length: '))
    temp = list(map(int, input('Enter list element seperated by Space: ').split()))
    main = []
    neg = []
    pos = []
    print('Processing...')
    for j in range(0, b) :
        if temp[j] < 0 :
            neg.append(temp[j])
        else :
            pos.append(temp[j])

    for j in range(0, b) :
        if len(pos) == 0 or j % 2 != 0 :
            main.append(neg.pop(0))
        else :
            main.append(pos.pop(0))
    for item in main :
        print(item, end=" ")
        
