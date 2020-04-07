import sqlite3
conn= sqlite3.connect('mydb1')
data={'name':['poplu'],'address':['barf khana']}
fields = data.keys()
vals = []
for v in fields:
    vals.append(data[v])
#conn.execute('insert into holler(name,address) values("%s","%s")' %(fields,vals))
r=conn.execute('select * from holler')
m=r.fetchall()
print(m)
conn.commit()
conn.close()
