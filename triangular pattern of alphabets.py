size = 5
letter = 65
for i in range(0, size + 1):
    for j in range(0, i):
        character = chr(letter)
        print(character, end='')
        letter += 1
    print()