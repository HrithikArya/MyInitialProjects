'''# to find area
l = int(input('enter length : '))
b = int(input('enter breadth : '))

if l==b:
    x = l**2  
    print('This is a Square of side',l,' whose Area is ', x)
else:
    y = l*b
    print('This is a Rectangle of length ', l, ' & breadth ',b,' whose Area is ',y)
'''

    
while True:
    q = int(input('''select any option to proceed:
    1. Area of Square
    2. Area of Rectangle
    3. Area of Triangle
    4. Area of Circle
    '''))
    if q==1:
        w = int(input('Enter the side : '))
        print('Area is : ', w**2)
    elif q==2:
        e = int(input('Enter lenght : '))
        r = int(input('Enter breadth : '))
        print('Area is : ', e*r)
    elif q==3:
        t = int(input('Enter Base : '))
        y = int(input('Enter Height : '))
        print('Area is : ', 1/2*t*y)
    elif q==4:
        u = int(input('Enter Radius : '))
        print('Area is : ', 22/7*u*u)
    else:
        print('INVALID INPUT')
    i = int(input('''enter your wish:
    1. for new calculation
    2. for ending
    '''))
    if i==2:
        break
#if __name__ == '__main__':main()
