import time

BASE_DIR = '/Users/moshekagan/Documents/idc/submitions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #2-28462.zip'
NUMBER_OF_ASSIGNMENT = 2

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

DO_IT_FROM_BEGIN = True
CHECK_EACH_STUDENT = True

ASSIGNMENTS_NAMES_AND_INPUTS = {
    "Ex2_practice_basic.py": [None],
    "Ex2_1_palindrome.py": [[123321], [123456]],
    "Ex2_2_common_denominators": [[10, 2, 5]]
}

CSV_FILE_PATH = BASE_SUB_DIR + "/students_res_%s.csv" % NUMBER_OF_ASSIGNMENT
timestamp = str(int(time.time()))
CSV_BACKUP_FILE_PATH = "/Users/moshekagan/Desktop/idc_res_backups/students_res_%s_%s.csv" % (NUMBER_OF_ASSIGNMENT, timestamp)


