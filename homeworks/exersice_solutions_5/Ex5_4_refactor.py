user_input = input("insert: ")

number = int(user_input)
is_palindrome = True

while number // 10 != 0:
    number_length = 0
    temp_number = number

    while temp_number // 10 != 0:
        temp_number = temp_number // 10
        number_length += 1

    last_digit = number % 10
    first_digit = number // 10 ** number_length

    if last_digit != first_digit and first_digit != 0:
        is_palindrome = False

    number = number // 10 % 10 ** (number_length - 1)

print(is_palindrome)
