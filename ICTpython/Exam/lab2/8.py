a = int(input())
b = int(input())
c = int(input())
t = min(a,b,c)
r = max(a,b,c)
s = a+b+c-t-r
print(str(t)+" "+str(s)+" "+str(r))
