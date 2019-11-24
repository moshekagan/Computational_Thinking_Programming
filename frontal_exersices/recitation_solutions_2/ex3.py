FIRST_DEGREE = 5000
SECOND_DEGREE = 15000
THIRD_DEGREE = 30000

SECOND_DEGREE_RATE = 0.10
THIRD_DEGREE_RATE = 0.30
FOURTH_DEGREE_RATE = 0.48

HEALTH_TAX_RATE = 0.05

age = int(input("What is your age? "))
salary = int(input("What is your monthly salary? "))

health_tax = 0
if age >= 18:
    health_tax = salary * HEALTH_TAX_RATE
    salary = salary - health_tax

tax = 0

if FIRST_DEGREE <= salary and salary < SECOND_DEGREE:
    second_degree_tax = (salary - FIRST_DEGREE) * SECOND_DEGREE_RATE

    tax = second_degree_tax
elif salary < THIRD_DEGREE:
    second_degree_tax = (SECOND_DEGREE - FIRST_DEGREE) * SECOND_DEGREE_RATE
    third_degree_tax = (salary - SECOND_DEGREE) * THIRD_DEGREE_RATE

    tax = third_degree_tax + second_degree_tax
elif THIRD_DEGREE <= salary:
    second_degree_tax = (SECOND_DEGREE - FIRST_DEGREE) * SECOND_DEGREE_RATE
    third_degree_tax = (THIRD_DEGREE - SECOND_DEGREE) * THIRD_DEGREE_RATE
    fourth_degree_tax = (salary - THIRD_DEGREE) * FOURTH_DEGREE_RATE

    tax = fourth_degree_tax + third_degree_tax + second_degree_tax

net_salary = salary - tax
print("Your net salary is: " + str(net_salary))
