number = int(input("Insert number with 3 digits: "))

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

digits_multiplication = first_digit * second_digit * third_digit
digits_sum = first_digit + second_digit + third_digit

print(digits_multiplication <= digits_sum and first_digit > third_digit)
