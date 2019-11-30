import time

BASE_DIR = '/Users/moshekagan/Documents/idc/submitions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #3-30848.zip'
NUMBER_OF_ASSIGNMENT = 3

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

DO_IT_FROM_BEGIN = True
CHECK_EACH_STUDENT = True

ASSIGNMENTS_NAMES_AND_INPUTS = {
    "Ex3_1_practice_basics.py": [None],
    "Ex3_2_seasons.py": [[11012019], [11081990], [31091000]],
    "Ex3_3_resturant.py": [[4, 1, 1, 1, 0.1, "True", "False"], [45, 1, 2, 1, 0.12, "False", "False"], [1, 1, 1, 1, 0, "True", "True"], [1, 1, 1, 1, 0, "False", "True"]]
}

CSV_FILE_PATH = BASE_SUB_DIR + "/students_res_%s.csv" % NUMBER_OF_ASSIGNMENT
timestamp = str(int(time.time()))
CSV_BACKUP_FILE_PATH = "/Users/moshekagan/Desktop/idc_res_backups/students_res_%s_%s.csv" % (NUMBER_OF_ASSIGNMENT, timestamp)


