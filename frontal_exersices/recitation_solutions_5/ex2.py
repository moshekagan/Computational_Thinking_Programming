size = int(input("Insert list size: "))
search = [None] * size

for i in range(0, len(search)):
    search[i] = float(input(str(i + 1) + ". Insert number:"))

number = float(input("Insert a number to check if exist in list: "))

is_in_list = False

for i in range(0, len(search)):
    if number == search[i]:
        is_in_list = True

if is_in_list is True:
    print(str(number) + " is in the list " + str(search))
else:
    print(str(number) + " is NOT in the list " + str(search))


