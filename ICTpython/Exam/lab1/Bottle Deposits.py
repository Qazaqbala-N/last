a = map(float, input().split())
k = float(0)
for i in a:
    if float(i) <= 1:
        k += 0.10
    else:
        k += 0.25
print("$" + str(k))
