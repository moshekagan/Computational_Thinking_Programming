import os
import importlib
import sys
import zipfile
from unittest.mock import patch

import mock


def remove_zip_extention(zip_file_name):
    return zip_file_name.split(".zip")[0]


BASE_DIR = '/Users/kaganmoshe/Documents/IDC/submmisions'

# INPUTS:
ZIP_FILE_NAME = 'Computational Thinking and Programming-26002-20201 - 200583-Exercise #1-25896.zip'
NUMBER_OF_ASSIGNMENT = 1

SUB_DIR_NAME = 'Exercise_' + str(NUMBER_OF_ASSIGNMENT)
BASE_SUB_DIR = BASE_DIR + "/" + SUB_DIR_NAME
MAIN_ZIP_FILE = BASE_DIR + "/" + ZIP_FILE_NAME

assignments_names_and_inputs = {
    "Ex1_1_square.py": None,
    "Ex1_2_name.py": ["Moshe Kagan"],
    "Ex1_3_circle.py": [10],
    "Ex1_4_restaurant.py": [10, 1, 1, 1, 0.1],
}
assignments_names = list(assignments_names_and_inputs.keys())

assignments_result_template = {}
for a in assignments_names:
    assignments_result_template[a] = None


def extract_zip_file(zip_file, path_where_to_extract):
    my_zipfile = zipfile.ZipFile(zip_file, mode='r')
    my_zipfile.extractall(path_where_to_extract)
    my_zipfile.close()


def extract_submissions(base_subdir):
    for root, subdirs, filenames in os.walk(base_subdir):
        for subdir in subdirs:
            if not subdir.startswith('__'):
                submission_dir_wrapper = base_subdir + '/' + subdir
                for submission_root, submission_subdirs, submission_filenames in os.walk(submission_dir_wrapper):
                    for file in submission_filenames:
                        if file.endswith('.zip'):
                            old_zip_file = submission_dir_wrapper + '/' + file
                            new_zip_file = base_subdir + '/' + file
                            os.rename(old_zip_file, new_zip_file)
                            print("Moved %s to %s" % (old_zip_file, new_zip_file))

                            print("About to rm: %s" + submission_dir_wrapper)
                            os.rmdir(submission_dir_wrapper)

                            print("About to extract zip file and remove it")
                            my_zipfile = zipfile.ZipFile(new_zip_file, mode='r')
                            my_zipfile.extractall(remove_zip_extention(new_zip_file))
                            my_zipfile.close()
                            os.remove(new_zip_file)


def run_python_script(python_script_path, inputs=None):
    with mock.patch('builtins.input', side_effect=inputs):
        exec(open(python_script_path).read())


def run_assignments(base_dir):
    assignments_results = {}
    for root, subdirs, filenames in os.walk(base_dir):
        for subdir in sorted(subdirs):
            if subdir.startswith('Ex' + str(NUMBER_OF_ASSIGNMENT)):
                assignments_results[subdir] = run_all_student_assignments(base_dir, subdir)

    print("Assignments results " + str(len(assignments_results)) + ": ")
    print(assignments_results)

    for student, assignments in assignments_results.items():
        print(str(list(assignments_results.keys()).index(student)) + ". " + student)
        all_pass = True
        for assignment, res in assignments.items():
            if not res:
                all_pass = False
                print(assignment + " | Failed to run!")
        if all_pass:
            print("All pass :)")


def run_all_student_assignments(base_dir, student_dir):
    student_submission_dir_path = base_dir + "/" + student_dir
    student_assignments_result = assignments_result_template

    print("\n-----------------------------------\t\t\t" + student_dir + "\t\t\t-----------------------------------\n")

    for submission_root, submission_subdirs, submission_filenames in os.walk(student_submission_dir_path):
        for file in assignments_names_and_inputs:
            if file.endswith(".py") and file in submission_filenames:
                try:
                    run_python_script(submission_root + '/' + file, assignments_names_and_inputs[file])
                    student_assignments_result[file] = True
                except:
                    student_assignments_result[file] = False
                    print(student_dir + " | " + file + " | Failed | " + str(sys.exc_info()[0]))
            else:
                student_assignments_result[file] = False
                print(student_dir + " | " + file + " | File not exist! | " + str(sys.exc_info()[0]))

    return student_assignments_result


if not os.path.isdir(BASE_SUB_DIR):
    extract_zip_file(MAIN_ZIP_FILE, BASE_SUB_DIR)
    extract_submissions(BASE_SUB_DIR)

run_assignments(BASE_SUB_DIR)

