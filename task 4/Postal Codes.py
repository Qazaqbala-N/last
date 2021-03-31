def check(s):
    if len(s) != 6: return False
    ind = 1
    for i in s:
        if ind % 2 == 1 and ('A' <= i <= 'Z') == False:
            return False
        elif ind % 2 == 0 and ('0' <= i <= '9') == False:
            return False
        ind += 1
    return True


Posts = {'A': 'Newfoundland',
         'B': 'Nova Scotia',
         'C': 'Prince Edward Island',
         'E': 'New Brunswick',
         'G': 'Quebec',
         'H': 'Quebec',
         'J': 'Quebec',
         'K': 'Ontario',
         'L': 'Ontario',
         'M': 'Ontario',
         'N': 'Ontario',
         'P': 'Ontario',
         'R': 'Manitoba',
         'S': 'Saskatchwan',
         'T': 'Albertia',
         'V': 'British Columbia',

         'Y': 'Yukon'}
s = input()
if check(s) == False:
    print("Wrong enter")
else:
    if s[1] == '0':
        print("Rural", end=' ')
    else:
        print("Urban", end=' ')
    print("address in ", end='')
    if s[0] == 'X':
        print('Nunavut or Northwest Territories')
    else:
        print(Posts[s[0]])
