def abc():
    i=1
    while True:
        yield i
        i+=2
m=abc()
