# Constants:
WEIGHT_PRICE_PER_KG = 1
SHIPPING_FEE_PER_KG = 5
TIP_RATE = 0.10

# Getting inputs from user
item_price = float(input("What is the item price? "))
item_weight = float(input("What is the item weight? "))
shipping_distance = float(input("What is the shipping distance? "))
apartment_floor = int(input("What is the apartment floor? "))

# Calculation
total_shipping_price = item_price + item_price*TIP_RATE + item_weight*WEIGHT_PRICE_PER_KG + shipping_distance*SHIPPING_FEE_PER_KG

# Printing results
print("The total price for the shipping is " + str(total_shipping_price) + " NIS")
