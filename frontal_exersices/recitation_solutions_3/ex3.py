n = int(input("insert: "))
d = int(input("insert: "))

if d < 0 or d > 10:
    print("Invalid input!")
else:
    c = 0

    while n != 0:
        nd = n % 10

        if nd == d:
            c += 1

        n = n // 10

    print(c)
