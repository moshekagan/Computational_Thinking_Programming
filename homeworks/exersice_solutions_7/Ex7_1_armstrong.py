max_range = int(input("enter a number: "))

for num in range(0, max_range):
    length = 0
    temp = num

    while temp != 0:
        temp = temp // 10
        length += 1

    sum = 0
    temp = num

    while temp != 0:
        sum = sum + ((temp % 10) ** length)
        temp = temp // 10

    if sum == num:
        print(str(num) + " is Armstrong number")
