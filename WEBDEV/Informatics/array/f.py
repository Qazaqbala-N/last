n=int(input())
b=(input().split())
stop = True
s = 0
for i in range(1,len(b)-1):
    if int(b[i])>int(b[i-1]) and int(b[i])>int(b[i+1]) :
        s=s+1
print(s)

