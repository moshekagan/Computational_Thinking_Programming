base = int(input("Insert a base number: "))

while base < 1:
    base = int(input("Invalid input, Insert again a base number: "))

for i in range(base, 0, -1):
    stars = ''
    for j in range(0, i):
        stars = stars + '*'
    spaces = (base - i) * ' '
    line = spaces + stars

    print(line)
