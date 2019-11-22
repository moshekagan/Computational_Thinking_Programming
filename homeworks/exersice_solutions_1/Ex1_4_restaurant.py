MINUTE_PRICE = 2
APPETIZER_PRICE = 25
MAIN_DISH_PRICE = 44
DESSERT_PRICE = 32.5

time_in_restaurant = int(input("How long have you been in the restaurant? (in minutes) "))
appetizers = int(input("How many appetizers you order? "))
main_dishes = int(input("How many main dishes you order? "))
desserts = int(input("How many desserts you order? "))
tip = float(input("How much tip do you want to give the waiters? (in percentage) "))

total_price = time_in_restaurant*MINUTE_PRICE + appetizers*APPETIZER_PRICE + main_dishes*MAIN_DISH_PRICE + desserts*DESSERT_PRICE
total_price_with_tip = total_price + total_price * tip

print("The total price is: " + str(total_price_with_tip))
