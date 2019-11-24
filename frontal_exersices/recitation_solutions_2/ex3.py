FIRST_BRACKET = 5000
SECOND_BRACKET = 15000
THIRD_BRACKET = 30000

SECOND_BRACKET_RATE = 0.10
THIRD_BRACKET_RATE = 0.30
FOURTH_BRACKET_RATE = 0.48

HEALTH_TAX_RATE = 0.05

age = int(input("What is your age? "))
salary = int(input("What is your monthly salary? "))

health_tax = 0
if age >= 18:
    health_tax = salary * HEALTH_TAX_RATE
    salary = salary - health_tax

tax = 0

if FIRST_BRACKET <= salary and salary < SECOND_BRACKET:
    second_bracket_tax = (salary - FIRST_BRACKET) * SECOND_BRACKET_RATE

    tax = second_bracket_tax
elif salary < THIRD_BRACKET:
    second_bracket_tax = (SECOND_BRACKET - FIRST_BRACKET) * SECOND_BRACKET_RATE
    third_bracket_tax = (salary - SECOND_BRACKET) * THIRD_BRACKET_RATE

    tax = third_bracket_tax + second_bracket_tax
elif THIRD_BRACKET <= salary:
    second_bracket_tax = (SECOND_BRACKET - FIRST_BRACKET) * SECOND_BRACKET_RATE
    third_bracket_tax = (THIRD_BRACKET - SECOND_BRACKET) * THIRD_BRACKET_RATE
    fourth_bracket_tax = (salary - THIRD_BRACKET) * FOURTH_BRACKET_RATE

    tax = fourth_bracket_tax + third_bracket_tax + second_bracket_tax

net_salary = salary - tax
print("Your net salary is: " + str(net_salary))
