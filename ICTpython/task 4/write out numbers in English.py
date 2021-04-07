def check(s):
    if len(s) > 3 or len(s) <= 0: return False
    for i in s:
        if not ('0' <= i <= '9'): return False
    return True


digits = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
          '8': 'eight', '9': 'nine'}
decimal = {'0': '', '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fivety', '6': 'sixty', '7': 'seventy',
           '8': 'eighty', '9': 'ninety', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
           '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineten'}
s = input()
con = True
if not check(s):
    print("Wrong enter")
else:
    i = 0
    n = len(s)
    if n == 3:
        print(digits[s[i]] + ' hundred ', end='')
        i += 1
    if n >= 2:
        if s[i] + s[i + 1] in decimal:
            con = False
            print(decimal[s[i] + s[i + 1]])
        else:
            print(decimal[s[i]], end=' ')
        i += 1
    if n >= 1:
        if con:
            print(digits[s[i]])
