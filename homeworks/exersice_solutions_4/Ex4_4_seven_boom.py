number = int(input('Please insert a number: '))

for i in range(1, number + 1):
    if i % 7 == 0:
        print("Boom!")
    else:
        print(i)
