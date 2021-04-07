n = int(input())
ds = list(map(int, input().split()))
print(max(ds) - min(ds) - len(ds) + 1)