def tri(x, y, xc, xy, r):
    if (x - xc) ** 2 + (y - xy) ** 2 <= r ** 2:
        return "YES"
    else:
        return "NO"


x = float(input())
y = float(input())
xc = float(input())
xy = float(input())
r = float(input())
print(tri(x,y,xc,xy,r))