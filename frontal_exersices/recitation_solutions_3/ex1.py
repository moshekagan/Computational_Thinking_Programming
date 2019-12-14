even_counter = 0

pick = int(input("pick a number: "))

for i in range(0, pick):
    number = int(input('Insert a number: '))

    if number % 2 == 0:
        even_counter += 1


print(str(even_counter))



