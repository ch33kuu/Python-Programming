f=open(r'C:\Users\BHAVYA\Desktop\EXACKT\Excel1.csv','r')
r=f.read()
f.close()
d={}
data=r.split('\n')[:-1]
keys=data[0].split(',')
for i,k in enumerate(keys):
    d[k]=[ ]
    for j in data[1:]:
        d[k]+=[j.split(',')[i]]
print(d)

