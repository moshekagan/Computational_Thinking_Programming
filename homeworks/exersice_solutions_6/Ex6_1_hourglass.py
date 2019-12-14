base_size = int(input("Insert a base size (positive number): "))

while base_size < 1:
    base_size = int(input("Invalid input, insert again a base size (positive number): "))

for i in range(base_size, 0, -1):
    stars = ""
    for j in range(0, i):
        stars = stars + '* '
    spaces = (base_size - i) * ' '
    print(spaces + stars)

for i in range(1, base_size+1):
    stars = ""
    for j in range(0, i):
        stars = stars + '* '
    spaces = (base_size - i) * ' '
    print(spaces + stars)


