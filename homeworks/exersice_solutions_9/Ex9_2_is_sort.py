size = int(input("Insert a list size: "))

my_list = [None] * size

for i in range(0, len(my_list)):
    my_list[i] = float(input(str(i + 1) + ". insert a value: "))

print(str(my_list))

is_sorted = True
for i in range(1, len(my_list)):
    if my_list[i] < my_list[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted")
else:
    print("The list is not sorted")
