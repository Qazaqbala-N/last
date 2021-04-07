a, b, c = map(int, input().split())
print(str(min(a, b, c)) + str(a + b + c - min(a, b, c) - max(a, b, c)) + str(max(a, b, c)))
