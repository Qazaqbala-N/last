from random import randrange
dictionary = dict()
probability_theory = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78] 
for i in range(2, 13):
    dictionary[i] = 0
for i in range(0, 1000):
    n = randrange(1, 7)
    m = randrange(1, 7)
    sum = n + m
    for j in dictionary.keys():
        if j == sum:
            dictionary[j] += 1
for i, j in dictionary.items():
    print(str(i)+"    "+str(round(float(j/1000)*100, 1))+"    "+str(probability_theory[i-2]))