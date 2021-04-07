
for _ in range(int(input())):
    r = False
    s = str(input())
    for i in range(len(s)):
        if "".join(set(s))=="a":
            print("NO")
            r = True
            break

        t ="a"+s[0:]
        if t != t[::-1]:
            print("YES")
            print(t)
            r = True
            break
        else:
            print("YES")
            print(s+"a")
            break

