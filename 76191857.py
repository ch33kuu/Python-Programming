n = 3
m = 4
a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]=i*j
print(a)
    
