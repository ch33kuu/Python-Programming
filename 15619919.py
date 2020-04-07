class Abc():
    def __init__(self,k):
        self.s=k
        print('object created')
    def __del__(self):
        print('ye mar gya')
    def __repr__(self):
        return self.s
    def __str__(self):
        return 'mei'+self.s+'hu'
    def __len__(self):
        return len(self.s)
    def __getitem__(self,n):
        return self.s[n]
    def __sub__(self,n):
        pass
    def __call__(self):
        return self.s*4
x=Abc('python')
