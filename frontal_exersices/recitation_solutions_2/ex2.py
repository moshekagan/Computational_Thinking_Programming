number = int(input("Insert a 3 digits number: "))

first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10

is_middle_greater = second_digit > first_digit and second_digit > third_digit
is_middle_smaller = second_digit < first_digit and second_digit < third_digit

if is_middle_greater or is_middle_smaller:
    print(str(number) + " is extreme number.")
else:
    print(str(number) + " is NOT extreme number.")