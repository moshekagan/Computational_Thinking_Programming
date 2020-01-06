size = 9
example_list = [3, 4, 6, 7, 8, 0, -10, 123.1, 44.123]

print("All the elements:")
for i in range(0, size):
    print(str(example_list[i]))

print("First element: " + str(example_list[0]))
print("Last element: " + str(example_list[len(example_list) - 1]))
print("Fourth element: " + str(example_list[3]))

min_value = example_list[0]
for i in range(0, size):
    if example_list[i] < min_value:
        min_value = example_list[i]

print("Minimum value: " + str(min_value))
