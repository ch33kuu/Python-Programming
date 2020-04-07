d={'name':['a','b','c'],'subject':['python','python','java'],'ratings':[2,3,4]}
a=d['subject']
b=list(filter(lambda x: x =='python',a))
print(b)


