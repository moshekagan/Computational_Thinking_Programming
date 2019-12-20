base = int(input("Base: "))
power = int(input("Power: "))

if power == 0:
    print(1)

answer = base
increment = base

for i in range(0, power - 1):
    for j in range(0, base - 1):
        answer = answer + increment
    increment = answer

print(str(base) + "^" + str(power) + " = " + str(increment))
