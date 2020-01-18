rows = int(input("Insert a rows size:"))
columns = int(input("Insert a columns size:"))

matrix = [[0] * rows for i in range(columns)]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        matrix[i][j] = float(input("Insert a number into [" + str(i) + ", " + str(j) + "]: "))

print()
for i in range(0, len(matrix)):
    print()
    for j in range(0, len(matrix[i])):
        print(str(matrix[i][j]) + '\t\t', end="")

sum = 0

# top and bottom rows
for i in range(0, columns):
    sum += matrix[0][i]

    last_line_index = rows - 1
    sum += matrix[last_line_index][i]

# right and left columns
for j in range(1, rows - 1):
    sum += matrix[j][0]

    last_column_index = len(matrix[0]) - 1
    sum += matrix[j][last_column_index]

print("\n\nThe sum is: " + str(sum))


def print_smiley(amount_of_smilies):
    print(":) " * amount_of_smilies)
