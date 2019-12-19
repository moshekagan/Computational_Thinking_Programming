first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

length_1 = 0
temp = first_number
while temp > 0:
    length_1 += 1
    temp = temp // 10

length_2 = 0
temp = second_number
while temp > 0:
    length_2 += 1
    temp = temp // 10


if length_1 != length_2:
    print("Numbers length are not equal!")
else:
    new_number = 0
    location = 0
    while second_number > 0:
        left_digit_num_1 = first_number % 10
        left_digit_num_2 = second_number % 10

        new_number += (left_digit_num_2 * 10**location) + (left_digit_num_1 * 10 ** (location+1))

        location += 2
        first_number = first_number // 10
        second_number = second_number // 10

    print(new_number)
