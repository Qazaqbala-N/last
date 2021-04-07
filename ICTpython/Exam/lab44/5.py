s = input()
dictionary = dict()
dictionary = {
    'A' : "Newfoundland", 'B' : "Nova Scotia", 'C' : "Prince Edward Island", 'E' : "New Brunswick", 
    'G' : "Quebec", 'H' : "Quebec", 'J' : "Quebec", 'K' : "Ontaria", 'L' : "Ontaria", 'M' : "Ontaria",
    'N' : "Ontaria", 'P' : "Ontaria", 'R' : "Manitoba", 'S' : "Saskatchewan", 'T' : "Alberta",
    'V' : "British Columbia", 'X' : "Nunavut or Northwest Territeria", 'Y' : "Yukon"
}
if dictionary.get(s[0]) == None:
    print("Error")
else:
    if s[1] == '0':
        print("rural adress "+dictionary.get(s[0]))
    else:
        print("urban adress "+dictionary.get(s[0]))


