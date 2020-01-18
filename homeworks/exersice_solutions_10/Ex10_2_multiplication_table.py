rows = int(input("Insert a rows size:"))
columns = int(input("Insert a columns size:"))

if rows < 2 or columns < 2:
    print("Invalid input!")
    exit()

table = [[0] * rows for i in range(columns)]

# Fill first column
for i in range(1, len(table)):
    table[i][0] = int(input("Insert a number in [" + str(i) + "," + "0]: "))

# Fill first row
for i in range(1, len(table[0])):
    table[0][i] = int(input("Insert a number in [0" + "," + str(i) + "]: "))

for i in range(0, len(table)):
    print()
    for j in range(0, len(table[i])):
        print(str(table[i][j]) + '\t', end="")

for i in range(1, len(table)):
    for j in range(1, len(table[i])):
        table[i][j] = table[0][j] * table[i][0]

print()
for i in range(0, len(table)):
    print()
    for j in range(0, len(table[i])):
        print(str(table[i][j]) + '\t', end="")
