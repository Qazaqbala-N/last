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
for i in range(1, 6):
    dictionary["B"+str(i)] = str(randrange(1, 16))
    dictionary["I"+str(i)] = str(randrange(16, 31))
    dictionary["N"+str(i)] = str(randrange(31, 46))
    dictionary["G"+str(i)] = str(randrange(46, 61))
    dictionary["O"+str(i)] = str(randrange(61, 76))
print("B   I   N   G   O")
for i in range(1, 6):
    print(dictionary["B"+str(i)]+"  "+dictionary["I"+str(i)]+"  "+dictionary["N"+str(i)]+
    "  "+dictionary["G"+str(i)]+"  "+dictionary["O"+str(i)])