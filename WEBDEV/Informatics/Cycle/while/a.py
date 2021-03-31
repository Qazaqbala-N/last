a = int(input())
print(1)
print("\n".join([str(i) for i in range(1,a+1) for j in range(i) if j*j==i]))