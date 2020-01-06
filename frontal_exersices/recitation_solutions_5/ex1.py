SIZE = 5
even_list = [None]*SIZE

for i in range(0, len(even_list)):
    even_list[i] = int(input("Insert even number:"))
    while even_list[i] % 2 != 0:
        even_list[i] = int(input(str(even_list[i]) + " is't not even, insert even number:"))

print(str(even_list))
