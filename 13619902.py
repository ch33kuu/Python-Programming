try:
    a=eval(input('enter your age'))
    assert a>0,'Age must be positive'
except AssertionError as e:
    print(e)
raise(IndexError)

