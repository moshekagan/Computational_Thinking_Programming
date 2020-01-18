def calculate_new_number(number):
    new_number = 0
    position = 0

    while number > 0:
        digit = (number % 10 + 1) % 10
        number = number // 10
        new_number = new_number + 10**position*digit

        position += 1

    return new_number


number = int(input("Insert a number: "))

while number < 0:
    number = int(input("Invalid input! Insert a *positive* number: "))

print("The new number is: " + str(calculate_new_number(number)))
