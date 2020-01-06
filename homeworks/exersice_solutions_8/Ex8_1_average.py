size = int(input("Please insert the list size: "))
example_list = [None]*size

if size < 1:
    print("Invalid input!")
    exit()

sum_of_all = 0
for i in range(0, size):
    example_list[i] = int(input("Insert a number: "))
    sum_of_all += example_list[i]

print("Sum of all items: " + str(sum_of_all))
print("Average of all items: " + str(sum_of_all/size))

sum_of_divide_3 = 0
count_numbers_divide_3 = 0
for i in range(0, size):
    if example_list[i] % 3 == 0:
        print(str(example_list[i]) + " - divisible by 3")
        count_numbers_divide_3 += 1
        sum_of_divide_3 += example_list[i]

print("Sum of the items divisible by 3: " + str(sum_of_divide_3))
print("Average of the items divisible by 3: " + str(sum_of_divide_3/count_numbers_divide_3))
