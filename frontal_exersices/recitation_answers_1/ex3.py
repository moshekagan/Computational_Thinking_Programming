distance = float(input("What is the distance from A to B? "))
train_speed = float(input("What is the train speed? "))

time_in_hours = distance / train_speed
time_in_minutes = time_in_hours * 60

print("The time from A to B will be: " + str(time_in_minutes) + " minutes.")
