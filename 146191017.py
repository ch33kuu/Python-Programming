class Abc():
    def __init__(self):
        print('object created')
    def __del__(self):
        print('object deleted')
    def show(self):
        print('i am here')
x=Abc()
x.show()
del x
y=Abc()
y=10
