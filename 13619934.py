def kuchkar(x):
    def yewala():
        print('i am trying')
        x()
        print('you are decorated now')
    return yewala
@kuchkar
def simple():
    print('i am so simple')
