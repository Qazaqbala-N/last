a = int(input())
b = input().split()
print(" ".join([str(b[i]) for i in range(len(b)) if i%2==0]))