MINUTE_PRICE = 2
APPETIZER_PRICE = 25
MAIN_DISH_PRICE = 44
DESSERT_PRICE = 32.5


time_in_restaurant = int(input("How long have you been in the restaurant? (in minutes) "))
appetizers = int(input("How many appetizers did you order? "))
main_dishes = int(input("How many main dishes did you order? "))
desserts = int(input("How many desserts did you order? "))
tip = float(input("How much tip do you want to give to the waiters? (in percentage) "))

is_member_club = input("Do you have a membership? ")
is_happy_hour = input("Is it happy hour? ")

if is_member_club == "True":
    if is_happy_hour == "True":
        total_price = time_in_restaurant * MINUTE_PRICE + appetizers * APPETIZER_PRICE + main_dishes * MAIN_DISH_PRICE + desserts * DESSERT_PRICE
        total_price = total_price * 0.5
    else:
        if time_in_restaurant < 5:
            time_in_restaurant = 0
        else:
            time_in_restaurant = time_in_restaurant - 5
        total_price = time_in_restaurant * MINUTE_PRICE + appetizers * APPETIZER_PRICE + main_dishes * MAIN_DISH_PRICE + desserts * DESSERT_PRICE
elif is_happy_hour == "True":
    total_price = time_in_restaurant * MINUTE_PRICE + appetizers * APPETIZER_PRICE + main_dishes * MAIN_DISH_PRICE * 0.5 + desserts * DESSERT_PRICE
else:
    total_price = time_in_restaurant*MINUTE_PRICE + appetizers*APPETIZER_PRICE + main_dishes*MAIN_DISH_PRICE + desserts*DESSERT_PRICE

total_price_with_tip = total_price + total_price * tip

print("The total price is: " + str(total_price_with_tip))
