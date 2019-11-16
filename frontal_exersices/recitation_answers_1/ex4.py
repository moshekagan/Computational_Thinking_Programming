FINAL_EXAM_RATE = 0.60
ASSIGNMENTS_RATE = 0.30

final_exam_grade = int(input("Please enter final exam grade (0-100): "))

assignment1 = int(input("Please insert assignment 1 grade (0-100): "))
assignment2 = int(input("Please insert assignment 2 grade (0-100): "))
assignment3 = int(input("Please insert assignment 3 grade (0-100): "))
assignment4 = int(input("Please insert assignment 4 grade (0-100): "))

attendance_times = int(input("Please insert the times of attendance (0-10) "))

assignments_average = (assignment1 + assignment2 + assignment3 + assignment4) / 4
final_grade = final_exam_grade*FINAL_EXAM_RATE + assignments_average*ASSIGNMENTS_RATE + attendance_times

print("Your final grade is: " + str(final_grade))
