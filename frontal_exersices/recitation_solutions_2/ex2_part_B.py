number = int(input("Insert a 3 digits number: "))

# number = 213
first_digit = number // 100 # 2
second_digit = number // 10 % 10 # 21 % 10 -> 1
third_digit = number % 10 # 3

is_middle_greater = second_digit > first_digit and second_digit > third_digit # False
is_middle_smaller = second_digit < first_digit and second_digit < third_digit # True

if is_middle_greater or is_middle_smaller:
    print(str(number) + " is extreme number.")
else:
    print(str(number) + " is NOT extreme number.")

