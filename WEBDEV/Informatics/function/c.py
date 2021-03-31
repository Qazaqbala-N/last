def xor(a,b):
    return bool(a) != bool(b)
a ,b = (input().split())
print(1 if xor(int(a),int(b)) else 0)