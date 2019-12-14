carpet_size = int(input("Insert a carpet size: "))
char = input("Insert a character: ")

for a in range(0, carpet_size):
    for i in range(0, carpet_size):
        square_line = ""
        for j in range(0, carpet_size):
            square_line = square_line + char

        line = ""
        for k in range(0, carpet_size):
            line = line + square_line + '\t'

        print(line)

    print()
