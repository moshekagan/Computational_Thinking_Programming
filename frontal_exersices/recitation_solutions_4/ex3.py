number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

if digit // 10 != 0:
    print("Invalid input!")
else:
    location = 0
    new_number = 0

    while number > 0:
        current_digit = number % 10
        new_number += digit * 10**location + current_digit * 10**(location+1)
        location += 2
        number = number // 10

    print(new_number)
