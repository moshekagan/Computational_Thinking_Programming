base = int(input("Base: "))
power = int(input("Power: "))

if power == 0:
    increment = 1
else:
    positive_base = base
    if positive_base < 0:
        positive_base = positive_base * -1

    answer = positive_base
    increment = positive_base

    for i in range(0, power - 1):
        for j in range(0, positive_base - 1):
            answer = answer + increment
        increment = answer

    if base < 0 and power % 2 != 0:
        increment = increment * -1

print(str(base) + "^" + str(power) + " = " + str(increment))
