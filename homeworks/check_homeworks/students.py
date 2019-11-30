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
"Justin Cesman",
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


ALTERNATIVE_NAMES = {
"Amalia Sostin": "Amalia Sostin",
"Amit Bashan": "Amit Bashan",
"Amit Miro": "Amit Miro",
"Amit Weshler": "Amit Weshler",
"Ariel Arabian": "Ariel Arabian",
"Baila Sherbin": "Baila Sherbin",
"Ben Dagan": "Ben Dagan",
"Ben Levy": "Ben Levy",
"Bernardo Marcushamer": "Bernardo Marcushamer",
"Carla Ghanem": "Carla Ghanem",
"Clement Hassid": "Clement Hassid",
"Daniel Zanzuri": "Daniel Zanzuri",
"David Myara": "David Myara",
"Edan Dooga": "Edan Dooga",
"Eli Kreisberger": "Eli Kreisberger",
"Elodie Miara": "Elodie Miara",
"Emanuel Siyoni": "Emanuel Siyoni",
"Emily Yahav": "Emily Yahav",
"Eyal Ephrati": "Eyal Ephrati",
"Frederico Filho": "Frederico Filho",
"Gabriel Itkowitz": "Gabriel Itkowitz",
"Gomezyani Joshua Gondwe": "Gomezyani Joshua Gondwe",
"Hannibal Jagdfeld": "Hannibal Jagdfeld",
"Hezekiah Bird": "Hezekiah Bird",
"Holden Hirsch": "Holden Hirsch",
"Jacob Freund": "Jacob Freund",
"Janhavi Pawar": "Janhavi Pawar",
"Jason Gellman": "Jason Gellman",
"Jaydin Pina": "Jaydin Pina",
"Jeremy Benhamou": "Jeremy Benhamou",
"Jeremy Hasson journo": "Jeremy Hasson",
"Jeremy Hasson": "Jeremy Hasson",
"Joey Azizoff": "Joey Azizoff",
"Jonathan Dar": "Jonathan Dar",
"Jonathan Siles": "Johnathan Siles",
"Johnathan Siles": "Johnathan Siles",
"Joy Avgi": "Joy Avgi",
"JustinDavid Cesman": "JustinDavid Cesman",
"Justin David Cesman": "Justin Cesman",
"Justin Cesman": "Justin Cesman",
"Leah Cohen": "Leah Cohen",
"Lotan Davidyan": "Lotan Davidyan",
"Maya Ivgy": "Maya Ivgy",
"Nathan Birmaher": "Nathan Birmaher",
"Nikola Dumanov": "Nikola Dumanov",
"Nir Klaiman": "Nir Klaiman",
"Niv Ram": "Niv Ram",
"Noa Chabbat": "Noa Chabbat",
"Noah Marks": "Noah Marks",
"Noe Zenaty": "Noe Zenaty",
"Noya Avraham": "Noya Avraham",
"Omri Herzikowitz": "Omri Herzikowitz",
"Peleg Somech": "Peleg Somech",
"Rebecca g y Wong": "Rebecca Wong",
"Rebecca Wong": "Rebecca Wong",
"Reut Damari": "Reut Damari",
"Ron Goldberg": "Ron Goldberg",
"Rotem Cohen": "Rotem Cohen",
"Roy Barokas": "Roy Barokas",
"Sasha Berdah": "Sasha Berdah",
"Shalem Raz": "Shalem Raz",
"Shlomoaryeh Kroopnick": "Shlomoaryeh Kroopnick",
"Sion Gadeloff": "Sion Gadeloff",
"Stav Harel": "Stav Harel",
"Stu Shapiro": "Stuart Shapiro",
"Stuart Shapiro": "Stuart Shapiro",
"Tali Miller": "Tali Miller",
"Violet Chibuta": "Violet Chibuta",
"Yam Kohen": "Yam Kohen",
"Yana Kroul": "Yana Kroul",
"Yehudah Berman": "Yehudah Berman",
"Yiduo Xu": "Yiduo Xu",
"Ynonn Habib": "Ynonn Habib",
"Yonatan Israeli": "Yonatan Israeli",
"Enrike Iliev": "Enrike Iliev",
"Eyal Zeev": "Eyal Zeev",
"Jude Apteker": "Jude Apteker",
"Pavlo Tabachnik": "Pavlo Tabachnik",
"Noam Manoah": "Noam Manoah",
}


def add_comment_to_student(student_name, comment):
    STUDENTS[ALTERNATIVE_NAMES[student_name]]["comments"].append(comment)


def set_grade_to_student(student_name, grade):
    STUDENTS[ALTERNATIVE_NAMES[student_name]]["grade"] = grade


def set_student_failed_to_check(student_name):
    STUDENTS[ALTERNATIVE_NAMES[student_name]]["failed_to_check"] = True


def set_zip_file_name(student_name, zip_file_name):
    STUDENTS[ALTERNATIVE_NAMES[student_name]]["zip_file_name"] = zip_file_name


def user_have_zip_file(student_name):
    return STUDENTS[ALTERNATIVE_NAMES[student_name]]["zip_file_name"] is not None


def set_student_results(student_name, result):
    STUDENTS[ALTERNATIVE_NAMES[student_name]]["ex_results"] = result


def get_student_comments(student_name):
    return STUDENTS[ALTERNATIVE_NAMES[student_name]]["comments"]


def save_students_result(file_name):
    print("Student results:")
    print(STUDENTS)
    export_to_csv(file_name, STUDENTS)
