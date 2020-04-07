a='hello'
b='bye'
a1=list(a)
for i in b:
    if i in a1:
        a1.remove(i)
print(a1)
a=''.join(a1)
print(a)
