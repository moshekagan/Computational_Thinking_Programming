def max_in_list(numbers):
    max_num = 0

    for i in range(0, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num


size = int(input("Insert a list size: "))
numbers_list = [None] * size
for i in range(0, len(numbers_list)):
    numbers_list[i] = int(input(str(i + 1) + ". Insert a number: "))

print(str(numbers_list))

maximum = max_in_list(numbers_list)

print("The maximun is: " + str(maximum))
