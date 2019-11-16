number = int(input("Please insert a 5 digit number: "))

digit_1 = number // 100000
digit_2 = (number // 10000) % 10
digit_3 = (number // 1000) % 10
digit_4 = (number % 1000) // 100
digit_5 = (number % 100) // 10
digit_6 = number % 10

is_first_and_last_equal = digit_1 == digit_6
is_second_and_1_before_last_equal = digit_2 == digit_5
is_third_and_2_before_last_equal = digit_3 == digit_4

print(is_first_and_last_equal and is_second_and_1_before_last_equal and is_third_and_2_before_last_equal)