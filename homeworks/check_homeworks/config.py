import time

BASE_DIR = '/Users/moshekagan/Documents/idc/submitions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #4-32977.zip'
NUMBER_OF_ASSIGNMENT = 4

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

DO_IT_FROM_BEGIN = False
CHECK_EACH_STUDENT = True

ASSIGNMENTS_NAMES_AND_INPUTS = {
    "Ex4_1_abs.py": [[5, 10], [5, 5]],
    "Ex4_2_shares.py": [[5, 'no', 1], [21, 'yes', 10], [20, 'yess', 100], [35, 'yes', 6]],
    "Ex4_3_square_loop.py": [[7]],
    "Ex4_4_seven_boom .py": [[15]]
}

CSV_FILE_PATH = BASE_SUB_DIR + "/students_res_%s.csv" % NUMBER_OF_ASSIGNMENT
timestamp = str(int(time.time()))
CSV_BACKUP_FILE_PATH = "/Users/moshekagan/Desktop/idc_res_backups/students_res_%s_%s.csv" % (NUMBER_OF_ASSIGNMENT, timestamp)


