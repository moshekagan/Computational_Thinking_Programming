def length_number(number):
    length = 0

    while number > 0:
        number = number // 10
        length += 1

    return length


number = int(input("Insert a number: "))
print("The length of the number is: " + str(length_number(number)))
