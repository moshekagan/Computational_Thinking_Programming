from homeworks.check_homeworks.config import BASE_SUB_DIR, NUMBER_OF_ASSIGNMENT
from homeworks.check_homeworks.export_student_resualt_to_csv import export_to_csv

STUDENTS_NAME = [
"Amalia Sostin",
"Amit Bashan",
"Amit Miro",
"Amit Weshler",
"Ariel Arabian",
"Baila Sherbin",
"Ben Dagan",
"Ben Levy",
"Bernardo Marcushamer",
"Carla Ghanem",
"Clement Hassid",
"Daniel Zanzuri",
"David Myara",
"Edan Dooga",
"Eli Kreisberger",
"Elodie Miara",
"Emanuel Siyoni",
"Emily Yahav",
"Eyal Ephrati",
"Frederico Filho",
"Gabriel Itkowitz",
"Gomezyani Joshua Gondwe",
"Hannibal Jagdfeld",
"Hezekiah Bird",
"Holden Hirsch",
"Jacob Freund",
"Janhavi Pawar",
"Jason Gellman",
"Jaydin Pina",
"Jeremy Benhamou",
"Jeremy Hasson",
"Joey Azizoff",
"Jonathan Dar",
"Johnathan Siles",
"Joy Avgi",
"JustinDavid Cesman",
"Leah Cohen",
"Lotan Davidyan",
"Maya Ivgy",
"Nathan Birmaher",
"Nikola Dumanov",
"Nir Klaiman",
"Niv Ram",
"Noa Chabbat",
"Noah Marks",
"Noe Zenaty",
"Noya Avraham",
"Omri Herzikowitz",
"Peleg Somech",
"Rebecca Wong",
"Reut Damari",
"Ron Goldberg",
"Rotem Cohen",
"Roy Barokas",
"Sasha Berdah",
"Shalem Raz",
"Shlomoaryeh Kroopnick",
"Sion Gadeloff",
"Stav Harel",
"Stuart Shapiro",
"Tali Miller",
"Violet Chibuta",
"Yam Kohen",
"Yana Kroul",
"Yehudah Berman",
"Yiduo Xu",
"Ynonn Habib",
"Yonatan Israeli",
"Enrike Iliev",
"Eyal Zeev",
"Jude Apteker",
"Pavlo Tabachnik",
"Noam Manoah",
]


STUDENTS = {}
for name in STUDENTS_NAME:
    STUDENTS[name] = {"name": name, "grade": None, "zip_file_name": None, "comments": [], "failed_to_check": False, "ex_results": None,}


def add_comment_to_student(student_name, comment):
    STUDENTS[student_name]["comments"].append(comment)


def set_grade_to_student(student_name, grade):
    STUDENTS[student_name]["grade"] = grade


def set_student_failed_to_check(student_name):
    STUDENTS[student_name]["failed_to_check"] = True


def set_zip_file_name(student_name, zip_file_name):
    STUDENTS[student_name]["zip_file_name"] = zip_file_name


def user_have_zip_file(student_name):
    return STUDENTS[student_name]["zip_file_name"] is not None


def set_student_results(student_name, result):
    STUDENTS[student_name]["ex_results"] = result


def get_student_comments(student_name):
    return STUDENTS[student_name]["comments"]


def save_students_result(file_name):
    print("Student results:")
    print(STUDENTS)
    export_to_csv(file_name, STUDENTS)
