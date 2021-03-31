text = input("Enter message: ")
Characters = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}
for n in text:
    n = n.upper()
    for i, j in Characters.items():
        for k in j:
            if k == n:
                for t in range(j.index(n) + 1):
                    print(i, end="")
