class Abc():
    print('henlo')
    a=10
    b=3.5
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
class Pqr(Xyz):
    def go(self):
        print('its pqr')
k=Pqr()
k.show()
k.go()
class Zxy(Pqr):
    def ekar(self):
        print('zxy')
z=Zxy()
class Aaa():
    def aa(self):
        print('aaa')    
class Mmm(Xyz,Aaa):
    def mm(self):
        print('mmm')
class Kuch(Xyz):
    def show(self):
        print('kuch bhi')
i=Kuch()
i.show()
i.do(3)
