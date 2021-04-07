points = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
          2: ['D', 'G'],
          3: ['B', 'C', 'M', 'P'],
          4: ['F', 'H', 'V', 'W', 'Y'],
          5: ['K'],
          8: ['J', 'X'],
          10: ['Q', 'Z']}
n = input()
cnt = 0
for t in n:
    for i, j in points.items():
        for k in j:
            if k == t:
                cnt += i
print(cnt)
