def kuchkar(x):
    def yewala():
        print('i am trying')
        x()
        print('you are decorated now')
    return yewala
def simple():
    print('i am so simple')
simple = kuchkar(simple)
simple = kuchkar(simple)
