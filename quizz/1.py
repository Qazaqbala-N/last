a = list(input())
b = list(input())
if a == b:
    print('-1')
elif len(a) == len(b):
    print(len(a))
else:
    print(max(len(a), len(b)))
#print(max)