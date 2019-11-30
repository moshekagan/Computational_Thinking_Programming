from homeworks.check_homeworks.config import ASSIGNMENTS_NAMES_AND_INPUTS

NEW_LINE = '\n'


def export_to_csv(file_name, students):
    f = open(file_name, "w+")

    _create_header(f)

    for name, student in students.items():
        _save_student(f, name, student)

    f.close()


def create_backup_csv(file_name):
    f = open(file_name, "w+")
    _create_header(f)
    f.close()


def save_student_into_backup(file_name, name, student):
    f = open(file_name, "a+")
    _save_student(f, name, student)
    f.close()


def _save_student(f, name, student):
    student_row = [student["name"], student["grade"], student["zip_file_name"], student["failed_to_check"]]

    for ex_name, inputs in ASSIGNMENTS_NAMES_AND_INPUTS.items():
        student_row.append(
            student["ex_results"][ex_name] if student["ex_results"] and student["ex_results"][ex_name] else False)

    student_row.append(' | '.join(str(v) for v in student["comments"]))
    f.write(','.join(str(v) for v in student_row) + NEW_LINE)


def _create_header(f):
    header = ["name", "grade", "zip_file_name", "failed_to_check"]

    for ex_name, inputs in ASSIGNMENTS_NAMES_AND_INPUTS.items():
        header.append(ex_name)
    header.append("comments")
    f.write(','.join(str(v) for v in header) + NEW_LINE)