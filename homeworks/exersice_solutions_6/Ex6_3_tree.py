tree_size = int(input("Insert a tree height: "))

for k in range(0, tree_size):
    for i in range(1, tree_size+1):
        stars = ""
        for j in range(0, i):
            stars = stars + '* '
        spaces = (tree_size - i) * ' '
        print(spaces + stars)

for k in range(0, tree_size):
    print((tree_size - 1) * " " + "*")
