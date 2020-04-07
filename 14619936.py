class Abc():
    print('henlo')
    a=10
    b=3.5
x=Abc()
class Xyz():
    a=10
    b=20
    def show(self):
        print("show")
        print(self.a,Abc.b)
    def do(self,k):
        self.a+=k
        Abc.b+=(k*2)
m=Xyz()
m.show()
