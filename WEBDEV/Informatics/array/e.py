n=int(input())
b=(input().split())
stop = True
for i in range(1,len(b)):
    if int(b[i])*int(b[i-1])>0 and stop:
        print("YES")
        stop=False
if stop:
    print("NO")
