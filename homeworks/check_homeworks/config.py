import time

BASE_DIR = '/Users/moshekagan/Documents/idc/submitions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #8-41802.zip'
NUMBER_OF_ASSIGNMENT = 8

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

DO_IT_FROM_BEGIN = False
CHECK_EACH_STUDENT = True

ASSIGNMENTS_NAMES_AND_INPUTS = {
    "Ex8_1_basic.py": [[]],
    "Ex8_2_average.py": [[5, 2, 3, 30, 6, 5], [0]]
}

CSV_FILE_PATH = BASE_SUB_DIR + "/students_res_%s.csv" % NUMBER_OF_ASSIGNMENT
timestamp = str(int(time.time()))
CSV_BACKUP_FILE_PATH = "/Users/moshekagan/Desktop/idc_res_backups/students_res_%s_%s.csv" % (NUMBER_OF_ASSIGNMENT, timestamp)


