a =str(input())
a =a[::-1]
x = 0
for (i) in range(0,len(a)):
    x=x+int(a[i])*2**int(i)
print(x)