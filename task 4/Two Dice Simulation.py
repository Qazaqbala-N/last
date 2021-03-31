import random


def randomSumOfTwoDiceRoll():
    return (random.randint(1, 6)) + (random.randint(1, 6))


total = {i: 0 for i in range(2, 13)}
for i in range(1000):
    total[randomSumOfTwoDiceRoll()] += 1
counts = [int(0) for i in range(11)]
for i in range(2, 13):
    for j in range(1, 7):
        if i - j <= 0: break
        if i - j <= 6:
            counts[i - 2] += 1
print("Total " + "\t" + " Simulated " + "\t" + " Excepted")
for k, v in total.items():
    print(str(k) + "\t\t" + str(v / 10) + "\t\t" + str(round(counts[k - 2] * 2.78, 2)))
