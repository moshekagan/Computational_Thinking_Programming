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


example_list = [None]*3
# example_list = [None, None, None]
example_list[0] = 100
example_list[1] = 200
example_list[2] = 300
example_list[3] = 400 # IndexError: list assignment index out of range


