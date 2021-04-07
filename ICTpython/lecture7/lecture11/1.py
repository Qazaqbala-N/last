def swap_case(s):
    for i in range(s.length()+1):
        if s[i] == s[i].upper():
            s[i]=s[i].lower()
        else:
            s[i]=s[i].upper()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)