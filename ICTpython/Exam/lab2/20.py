a, b = map(int, input().split())
t = [1 for i in range(a)]
while (b != 0):
    l, r = map(int, input().split())
    for i in range(l - 1, r):
        t[i] = 0
    b -= 1
for i in t:
    if i == 0:
        print(".", end="")
    else:
        print("I", end="")
