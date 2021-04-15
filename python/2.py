for _ in range(int(input())):
    a = int(input())
    b = []
    for i in range(1,a+1):
        g = int(input())
        b.append(g)

    c=set(b)
    if c[0] == b[0] and c[0] == b[a]:
        for i in range(1,a+1):
            if c[1]==b[i]:
                print(i)
    else:
        if c[0]==b[i]:
            print(i)