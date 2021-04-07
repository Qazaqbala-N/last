a = int(input())
i = 0
s = []
while 2**i<=a:
    s.append(2**i)
    i = i + 1
print(" ".join(str(s[i]) for i in range(len(s))))