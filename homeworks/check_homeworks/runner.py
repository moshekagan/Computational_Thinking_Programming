import os
import shutil

from homeworks.check_homeworks.check_homeworks import run_assignments
from homeworks.check_homeworks.config import *
from homeworks.check_homeworks.export_student_resualt_to_csv import create_backup_csv
from homeworks.check_homeworks.extractor import extract_zip_file, extract_submissions
from homeworks.check_homeworks.students import STUDENTS, save_students_result


if DO_IT_FROM_BEGIN and os.path.isdir(BASE_SUB_DIR):
    shutil.rmtree(BASE_SUB_DIR)


if not os.path.isdir(BASE_SUB_DIR):
    extract_zip_file(MAIN_ZIP_FILE, BASE_SUB_DIR)
    extract_submissions(BASE_SUB_DIR)

if CHECK_EACH_STUDENT:
    create_backup_csv(CSV_BACKUP_FILE_PATH)

run_assignments(BASE_SUB_DIR, STUDENTS)

save_students_result(CSV_FILE_PATH)

