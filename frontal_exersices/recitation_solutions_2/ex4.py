even_counter = 0

for i in range(0, 5):
    number = int(input('Insert a number: '))

    if number % 2 == 0:
        even_counter = even_counter + 1

print("There are " + str(even_counter) + " even numbers")
