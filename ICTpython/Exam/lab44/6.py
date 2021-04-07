dictionary1 = dict()
dictionary2 = dict()
dictionary1 = dict()
dictionary1 = dict()
dictionary1 = {
    '1': "one hundred", '2': "two hundred", '3': "three hundred", '4': "four hundred",
    '5': "five hundred", '6': "six hundred", '7': "seven hundred", '8': "eight hundred", '9': "nine hundred"
}
dictionary2 = {
    '2': "twenty", '3': "thirty", '4': "forty", '5': "fifty", '6': "sixty",
    '7': "seventy", '8': "eighty", '9': "ninety", '0': ""
}
dictionary3 = {
    '0': "", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
    '7': "seven", '8': "eight", '9': "nine",
}
dictionary4 = {
    '0': "ten", '1': "eleven", '2': "twelve", '3': "thirteen", '4': "fourteen", '5': "fifteen",
    '6': "sixteen", '7': "seventeen", '8': "eighteen", '9': "nineteen",
}


def Numbers_in_English(m):
    s = str(m)
    if len(s) == 1:
        print(dictionary3.get(s[0]), end=" ")
    elif len(s) == 2:
        if s[0] != '1':
            print(dictionary2.get(s[0]), end=" ")
            print(dictionary3.get(s[1]), end=" ")
        else:
            print(dictionary4.get(s[1]), end=" ")
    else:
        print(dictionary1.get(s[0]), end=" ")
        if s[1] != '1':
            print(dictionary2.get(s[1]), end=" ")
            print(dictionary3.get(s[2]), end=" ")
        else:
            print(dictionary4.get(s[2]), end=" ")


n = int(input())
Numbers_in_English(n)
