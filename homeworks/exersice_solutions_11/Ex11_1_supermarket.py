BREAD = 10
MEAT = 40
CHOCOLATE = 15
BEER = 6

amount_of_bread = int(input("How many breads did you buy? "))
amount_of_meat = int(input("How many kilograms of meat did you buy? "))
amount_of_chocolate = int(input("How many chocolates did you buy? "))
amount_of_beer = int(input("How many beers did you buy? "))

final_price = 0

final_price += BREAD * amount_of_bread

if amount_of_chocolate > 2:
    final_price += (CHOCOLATE * 0.9) * amount_of_chocolate
else:
    final_price += CHOCOLATE * amount_of_chocolate

if amount_of_meat > 3:
    final_price += 30 * amount_of_meat
else:
    final_price += MEAT * amount_of_meat

if amount_of_beer < 12:
    final_price = BEER * amount_of_beer
elif amount_of_beer < 37:
    final_price = 5 * amount_of_beer
else:
    final_price = 4 * amount_of_beer


print("The final price is " + str(final_price) + " NIS")
