first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# find smaller
if first_number > second_number:
    smaller = second_number
else:
    smaller = first_number


hcf = 1

for i in range(1, smaller + 1):
    if first_number % i == 0 and second_number % i == 0:
        hcf = i

print("HCF = " + str(hcf))
