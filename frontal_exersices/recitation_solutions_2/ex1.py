ADULT = 18
PENSIONER = 65

age = int(input("Please insert your age: "))

if age < ADULT:
    print("Child")
elif age < PENSIONER:
    print("Adult")
else:
    print("Pensioner")
