c=34
try:
    a=int(input('enter'))
    b=c/a
except ValueError as e:
    print(e)
except ZeroDivisonError:
    print('aise kaise bhai')
else:
    print(c)
finally:
    print('class over')
