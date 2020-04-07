def abc(*a):
    c=0
    for i in a:
        c+=i
    return c
p=abc(5,6,7)
print(p)
