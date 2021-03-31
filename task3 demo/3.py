def div(n):
    k = 0
    for i in range(2,n+1):
        if n%i ==0 :
          k+=1
    if(k==1):
        return "YES"
    else:
        return "NO"
n = int(input())

print(div(n))
