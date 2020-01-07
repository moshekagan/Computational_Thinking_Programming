SIZE = 6

list1 = [None] * SIZE
list2 = [None] * SIZE

print("List1:")
for i in range(0, len(list1)):
    list1[i] = int(input(str(i+1) + ". insert a number: "))

print("List2:")
for i in range(0, len(list2)):
    list2[i] = int(input(str(i+1) + ". insert a number: "))

print("Common values:")
for i in range(0, len(list1)):
    is_in_list = False
    for j in range(0, len(list2)):
        if is_in_list:
            break
        if list1[i] == list2[j]:
            is_in_list = True
            print(str(list1[i]))
