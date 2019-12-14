APPL = "APPEL"
TESLA = "TESLA"
VISA = "VISA"
TEVA = "TEVA"
RISK_THRESHOLD = 5
YOUNG_AGE = 35

age = int(input("What is your age? "))
is_like_tech = input("Do you like technologies? ")
risk_level = int(input("What is your risk level (1-10)? "))

if age < 0 or (is_like_tech != "yes" and is_like_tech != "no") or not 1 <= risk_level <= 10:
    print("Invalid inputs!")
else:
    if is_like_tech == "yes":
        if risk_level < RISK_THRESHOLD:
            print("You should invest in " + APPL)
        elif age < YOUNG_AGE:
            print("You should invest in " + TESLA)
        else:
            print("Sorry, there is no recommendation for you")
    else:
        if risk_level < RISK_THRESHOLD:
            print("You should invest in " + VISA)
        else:
            print("You should invest in " + TEVA)
