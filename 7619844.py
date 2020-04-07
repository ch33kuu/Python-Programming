a=input('first')
b=input('second')
c=input('third')
if(a>=b):
    if(a>c):
        print('a is largest')
    if(c>a):
        print('c is largest')
elif(b>=a):
    if(b>c):
        print('b is largest')
    if(c>b):
        print('c is largest')
else:
    print('numbers are equal')
