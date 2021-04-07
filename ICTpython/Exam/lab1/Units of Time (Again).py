n = int(input())
d = int(n // (24 * 60 * 60))
n = n % (24 * 3600)
h = int(n // (60 * 60))
n = n % 360
m = int(n // 60)
s = int(n % 60)
print("d :" + str(d) + " :: h:" + str(h) + "  ::   m:" + str(m) + "  :: s:" + str(s))
