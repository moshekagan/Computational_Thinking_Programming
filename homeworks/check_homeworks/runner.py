import os
import shutil

from homeworks.check_homeworks.check_homeworks import run_assignments
from homeworks.check_homeworks.config import *
from homeworks.check_homeworks.extractor import extract_zip_file, extract_submissions
from homeworks.check_homeworks.students import STUDENTS, save_students_result

if DO_IT_FROM_BEGIN:
    shutil.rmtree(BASE_SUB_DIR)


if not os.path.isdir(BASE_SUB_DIR):
    extract_zip_file(MAIN_ZIP_FILE, BASE_SUB_DIR)
    extract_submissions(BASE_SUB_DIR)

run_assignments(BASE_SUB_DIR, STUDENTS)

save_students_result(BASE_SUB_DIR + "/students_res_%s.csv" % NUMBER_OF_ASSIGNMENT)

