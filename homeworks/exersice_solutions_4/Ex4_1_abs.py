x = float(input('Please insert the first number: '))
y = float(input('Please insert the second number: '))

result = x - y

if result < 0:
    result = result * -1

print("|" + str(x) + " - " + str(y) + "| = " + str(result))