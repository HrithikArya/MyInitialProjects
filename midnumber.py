# python
def MidNumber(arr) :
    ans = 0
    if len(arr)%2!=0 :
        ans = arr[((len(arr)+1)/2)-1]
    else :
        ans = arr[((len(arr))/2)-1]
    return ans

test_cases = int(input('Enter test cases: '))
for i in range(test_cases) :
    list1 = list(map(int, input('Enter list element seperated by spaces: ')))
    print(MidNumber(list1))