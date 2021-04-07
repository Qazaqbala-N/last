a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1*b1*c1 == a2*b2*c2:
    print("Equal")
elif a1 * b1 * c1 > a2 * b2 * c2:
    print("first bigger")
elif a1 * b1 * c1 < a2 * b2 * c2:
    print("second bigger"
          )
else:
    print("Incamparable")
