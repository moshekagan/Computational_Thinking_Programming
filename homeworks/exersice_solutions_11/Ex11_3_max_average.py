def calculate_average(row):
    if len(row) == 0:
        return 0

    row_sum = 0

    for i in range(len(row)):
        row_sum += row[i]

    return row_sum / len(row)


rows = int(input("Insert a rows size: "))
columns = int(input("Insert a columns size: "))

matrix = [[None]*columns for i in range(rows)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = float(input("Insert a number [" + str(i) + "," + str(j) + "]: "))

maximum_avg_index = 0
maximum_avg = calculate_average(matrix[0])

for i in range(len(matrix)):
    print(matrix[i])

    current_avg = calculate_average(matrix[i])
    if current_avg > maximum_avg:
        maximum_avg_index = i
        maximum_avg = current_avg


print("The maximum average is " + str(maximum_avg) + " and the row index is: " + str(maximum_avg_index))
