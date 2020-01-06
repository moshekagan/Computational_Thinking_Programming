num_1 = int(input("insert a number: "))
num_2 = int(input("insert a number: "))

res = 0
for i in range(0, num_2):
    res = num_1 + res

print(str(num_1) + ' * ' + str(num_2) + ' = ' + str(res))