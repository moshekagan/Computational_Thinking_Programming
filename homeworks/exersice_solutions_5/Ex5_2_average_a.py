iteration_number = int(input("How many number would you like to include in the average? "))

if iteration_number < 0:
    print("Invalid input!")
else:
    sum = 0

    for i in range(0, iteration_number):
        num = float(input("Insert a number: "))
        sum += num

    print("The average is: " + str(sum/iteration_number))
