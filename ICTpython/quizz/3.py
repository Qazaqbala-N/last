a, b = map(int, input().split())
cnt = 0
for i in range(1, a + 1):
    if b % i == 0 and (b / i) <= a:
        cnt = cnt + 1
print(cnt)
