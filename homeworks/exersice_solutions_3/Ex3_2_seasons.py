SPRING = "Spring"
SUMMER = "Summer"
AUTUMN = "Autumn"
WINTER = "Winter"

date = int(input("Insert a date: "))

day = date // 1000000
month = (date // 10000) % 100
year = date % 10000

if 3 <= month and month <= 5:
    season = SPRING
elif 6 <= month and month <= 8:
    season = SUMMER
elif 9 <= month and month <= 11:
    season = AUTUMN
else:
    season = WINTER

day = str(day)
month = str(month)
year = str(year)

print(day + '-' + month + '-' + year + " " + season)