string1 = 'hello'
string2 = 'bye'
def split(word):
    return list(word)
s3= split(string2)
i=str(s3)
if i in string1:
    string1.replace(i,'')
print(i)
