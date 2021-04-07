s = input().upper()
dictionary = dict()
dictionary = {
    1 : ".,?!:", 2 : "ABC", 3 : "DEF", 4 : "GHI", 
    5 : "JKL", 6 : "MNO", 7 : "PQRS", 8 : "TUV", 9 : "WXYZ", 0 : " "
}
count = 1
for i in range(0, len(s)):  
    for j in dictionary.keys():
        s1 = dictionary[j]
        for u in range(0, len(s1)):
            if s[i] == s1[u]:
                print(str(j)*count, end="")
                count = 1
                break
            count += 1
        count = 1