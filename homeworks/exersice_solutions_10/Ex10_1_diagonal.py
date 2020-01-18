SIZE = 5
matrix = [[0] * SIZE for i in range(SIZE)]


matrix[0][2] = 3
matrix[1][1] = 5

for i in range(0, len(matrix)):
    print(str(matrix[i]))

number = int(input("Insert a number: "))

# First diagonal
for i in range(0, len(matrix)):
    matrix[i][i] = number

# Second diagonal
for j in range(len(matrix[i]), 0, -1):
    matrix[len(matrix[i]) - j][j - 1] = number

for i in range(0, len(matrix)):
    print(str(matrix[i]))
