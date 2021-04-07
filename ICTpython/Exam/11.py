
n = int(input())
name = []
for i in range(1, n+1):
    r = input()
    if r in name:
        print("YES")
    else:
        print("NO")
        name.append(r)
