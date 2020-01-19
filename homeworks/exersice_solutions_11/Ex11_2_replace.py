def replace_digit(number, position, new_digit):
    current_position = 0
    new_number = 0
    while number > 0:
        current_digit = number % 10
        number = number // 10

        if current_position == position:
            current_digit = new_digit

        new_number = new_number + current_digit * 10**current_position

        current_position += 1
    return new_number


print(replace_digit(1234, 1, 9))
print(replace_digit(1234, 1, 0))
print(replace_digit(1234, 3, 0))
