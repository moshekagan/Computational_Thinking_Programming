import csv

with open('/Users/moshekagan/Documents/idc/recitation_attendance_16.1.2020.csv', newline="") as f:
    reader = csv.reader(f)
    dates = {
        '10/11/2019': 0,
        '17/11/2019': 1,
        '24/11/2019': 2,
        '01/12/2019': 3,
        '08/12/2019': 4,
        '15/12/2019': 5,
        '22/12/2019': 6,
        '31/12/2019': 7,
        '05/01/2020': 8,
        '12/01/2020': 9
    }

    students_names = []
    rows = []
    for row in reader:
        print(row)
        if row[1] == 'date':
            continue
        rows.append(row)
        student_name = row[2].lower().strip().title()

        if student_name not in students_names:
            students_names.append(student_name)

    students_names.sort()

    students_attendance = {}
    for student in students_names:
        students_attendance.update({student: [0]*11})
    # print(students_attendance)

    print(list(students_attendance.keys()))
    print(len(list(students_attendance.keys())))

    for row in rows:
        student_name = row[2].lower().strip().title()
        students_attendance[student_name][dates[row[1]]] = 1

    for name, att in students_attendance.items():
        count = 0
        for i in range(0, 10, 2):
            count += att[i] or att[i+1]
        students_attendance[name][10] = count

    print(students_attendance)

    header = ["name"] + list(dates.keys()) + ['count']
    attendance = [header]
    for name, att in students_attendance.items():
        attendance.append([name] + att)

    with open('/Users/moshekagan/Documents/idc/recitation_attendance_16.1.2020_output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(attendance)
