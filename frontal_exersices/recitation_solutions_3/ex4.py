num_1 = int(input("insert a number: "))
num_2 = int(input("insert a number: "))

result = 0
for k in range(0, num_1):
    result = result + num_2

print(str(num_1) + " * " + str(num_2) + " = " + str(result))
