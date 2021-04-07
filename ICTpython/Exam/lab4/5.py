s = input()
l = list(set(s))

if len(l) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')