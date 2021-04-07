s=input()
s2=input()
s=s.lower()
s2=s2.lower()
s3=set()
s4=set()
for i in s:
    if i!=' ' and i!='!' and i!=',' and i!='.' and i!='?':
        s3.add(i)
for i in s2:
    if i!=' ' and i!='!' and i!=',' and i!='.' and i!='?':
        s4.add(i)
if len(s3.intersection(s4))==len(s3) and len(s3.intersection(s4))==len(s4):
    print("Yes")
else:
    print("No")