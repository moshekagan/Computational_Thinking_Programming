number = int(input("Insert a number: "))
length = 0

while number != 0:
    length += 1
    number = number // 10

print(str(length))
