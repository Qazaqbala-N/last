a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (c == a + 2) and (d == b+1 or d == b-1):
    print("YES")
elif (c == a + 1) and (d == b+2 or d == b-2):
    print("YES")
elif (c == a - 1) and (d == b+2 or d == b-2):
    print("YES")
elif (c == a + 2) and ( d == b+1 or d == b-1):
    print("YES")
else:print("No")

