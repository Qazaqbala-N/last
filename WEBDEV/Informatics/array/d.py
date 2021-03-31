a = int(input())
b = input().split()
print(len([str(b[i]) for i in range(len(b)-1) if int(b[i])<int(b[i+1])]))