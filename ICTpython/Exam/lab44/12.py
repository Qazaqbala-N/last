from random import randrange
String = ['B', 'I', 'N', 'G', 'O']
dictionary = dict()
dictionary = {
    'B1' : "", 'B2' : "", 'B3' : "", 'B4' : "", 'B5' : "",
    'I1' : "", 'I2' : "", 'I3' : "", 'I4' : "", 'I5' : "",
    'N1' : "", 'N2' : "", 'N3' : "", 'N4' : "", 'N5' : "",
    'G1' : "", 'G2' : "", 'G3' : "", 'G4' : "", 'G5' : "",
    'O1' : "", 'O2' : "", 'O3' : "", 'O4' : "", 'O5' : "",
}
def winner(diction):
    sum = 0
    for j in String:
        for i in range(1, 6):
            sum += int(diction[j+str(i)])
        if sum == 0:
            return True
        sum = 0
    for i in range(1, 6):
        for j in String:
            sum += int(diction[j+str(i)])
        if sum == 0:
            return True
        sum = 0
    for i in range(1, 6):
        sum += int(diction[String[i-1]+str(i)])
    if sum == 0:
            return True
    else:
        sum = 0
    for i in range(5, 0, -1):
        sum += int(diction[String[i-1]+str(6-i)])
    if sum == 0:
            return True
    return False   
for i in range(1, 6):
    dictionary["B"+str(i)] = str(randrange(1, 16))
    dictionary["I"+str(i)] = str(randrange(16, 31))
    dictionary["N"+str(i)] = str(randrange(31, 46))
    dictionary["G"+str(i)] = str(randrange(46, 61))
    dictionary["O"+str(i)] = str(randrange(61, 76))
# for i in range(1, 6):
#     dictionary["B"+str(i)] = 0
for i in range(0, 15):
    n = randrange(1, 76)
    for j in dictionary.keys():
        if int(n) == int(dictionary[j]):
            dictionary[j] = str(0)
print(winner(dictionary))