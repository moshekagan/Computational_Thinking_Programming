num_1 = int(input("insert a number: "))
num_2 = int(input("insert a number: "))

result = 1
for k in range(0, num_2):
    result = result * num_1

print(str(num_1) + " ^ " + str(num_2) + " = " + str(result))
