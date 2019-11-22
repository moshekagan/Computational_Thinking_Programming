number = int(input("please insert a number: "))
first_denominator = int(input("please insert the first denominator: "))
second_denominator = int(input("please insert the second denominator: "))

is_common_denominators = number % first_denominator == 0 and number % second_denominator == 0

print("Are the numbers " + str(first_denominator) + " and " + str(second_denominator) + " are common denominators of " + str(number) + "? " +
      str(is_common_denominators is True))
