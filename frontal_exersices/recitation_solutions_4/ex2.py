dec_number = int(input("Enter a decimal number: "))

bin_number = ""

while dec_number > 0:
    if dec_number % 2 == 0:
        bin_number = "0" + bin_number
    else:
        bin_number = "1" + bin_number

    dec_number = int(dec_number / 2)

print(bin_number)
