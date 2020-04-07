import tkinter as tk
app=tk.Tk()
app.geometry('600x400')
app.title('Calculator')
a=tk.Entry(app)
a.place(x=10,y=2)
b=tk.Entry(app)
b.place(x=300,y=2)
#a.grid(row=0,column=0)
#a.place(x=50,y=10)
#b.place(x=100,y=10)
l=tk.Label(app,text=' ')
l.place(x=225,y=300)
def jod():
    a1=int(a.get())
    b1=int(b.get())
    l.configure(text=a1+b1)
    
c=tk.Button(app,text='+',command=jod)
c.place(x=200,y=90)
def ghata():
    a1=int(a.get())
    b1=int(b.get())
    l.configure(text=a1-b1)
    
c1=tk.Button(app,text='-',command=ghata)
c1.place(x=250,y=90)
def gunakar():
    a1=int(a.get())
    b1=int(b.get())
    l.configure(text=a1*b1)
    
c1=tk.Button(app,text='*',command=gunakar)
c1.place(x=200,y=140)
def bhagakar():
    a1=float(a.get())
    b1=float(b.get())
    l.configure(text=a1/b1)
    
c1=tk.Button(app,text='/',command=bhagakar)
c1.place(x=250,y=140)
app.mainloop()
