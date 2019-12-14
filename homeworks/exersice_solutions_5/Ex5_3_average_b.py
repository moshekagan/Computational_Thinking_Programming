END_COMMAND = 'end'

count = 0
sum_numbers = 0

num = input("Insert a number: ")

while num != END_COMMAND:
    count += 1
    sum_numbers += float(num)
    num = input("Insert a number: ")


if count == 0:
    print("Can't calculate average of 0 numbers")
else:
    print("The average is: " + str(sum_numbers/count))
