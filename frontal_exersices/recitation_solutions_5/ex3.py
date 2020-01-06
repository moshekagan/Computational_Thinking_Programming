divisors = [2, 5]

size = int(input("Insert a list size: "))
my_list = [None]*size

for i in range(0, len(my_list)):
    my_list[i] = int(input(str(i+1) + ". Insert number:"))

print(str(my_list))

for i in range(0, len(my_list)):
    is_divided = True

    for j in range(0, len(divisors)):
        if my_list[i] % divisors[j] != 0:
            is_divided = False

    if is_divided:
        print(str(my_list[i]) + " divided by: " + str(divisors) + " without reminder")
    else:
        print(str(my_list[i]) + " not divided by: " + str(divisors) + " without reminder")