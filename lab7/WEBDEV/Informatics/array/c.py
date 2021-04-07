a = int(input())
b = input().split()
print(len([str(b[i]) for i in range(len(b)) if int(b[i])>0 ]))