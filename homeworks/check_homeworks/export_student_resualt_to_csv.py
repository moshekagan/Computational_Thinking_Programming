from homeworks.check_homeworks.config import ASSIGNMENTS_NAMES_AND_INPUTS

NEW_LINE = '\n'


def export_to_csv(file_name, students):
    f = open(file_name, "w+")

    header = ["name", "zip_file_name", "failed_to_check"]

    for ex_name, inputs in ASSIGNMENTS_NAMES_AND_INPUTS.items():
        header.append(ex_name)
    header.append("comments")
    f.write(','.join(str(v) for v in header) + NEW_LINE)

    for name, student in students.items():
        student_row = [student["name"], student["zip_file_name"],  student["failed_to_check"]]

        for ex_name, inputs in ASSIGNMENTS_NAMES_AND_INPUTS.items():
            student_row.append(student["ex_results"][ex_name] if student["ex_results"] and student["ex_results"][ex_name] else False)

        student_row.append('| '.join(str(v) for v in student["comments"]))
        f.write(','.join(str(v) for v in student_row) + NEW_LINE)

    f.close()
