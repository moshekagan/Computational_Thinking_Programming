BASE_DIR = '/Users/moshekagan/Documents/idc/submitions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #1-25896.zip'
NUMBER_OF_ASSIGNMENT = 1

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

DO_IT_FROM_BEGIN = True
CHECK_EACH_STUDENT = True

ASSIGNMENTS_NAMES_AND_INPUTS = {
    "Ex1_1_square.py": None,
    "Ex1_2_name.py": ["Moshe Kagan"],
    "Ex1_3_circle.py": [10],
    "Ex1_4_restaurant.py": [10, 1, 1, 1, 0.1],
}
