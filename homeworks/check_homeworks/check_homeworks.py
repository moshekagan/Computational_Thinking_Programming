import os
import sys

import mock

from homeworks.check_homeworks.comments import PYTHON_FILE_DOES_NOT_EXIST
from homeworks.check_homeworks.config import *
from homeworks.check_homeworks.students import *


def run_assignments(base_dir, students):
    for student_name, student in students.items():
        if student["failed_to_check"] or len(student["comments"]) > 0 :
            continue

        print("\n-----------------------------------\t" + student_name)

        student_dir_path = base_dir + '/' + student_name

        if os.path.isdir(student_dir_path):
            result = _run_all_student_assignments(student_dir_path, student_name)
            set_student_results(student_name, result)
        else:
            set_student_failed_to_check(student_name)

        if CHECK_EACH_STUDENT:
            input("--------> Next? ")


def _get_exercise_number_prefix(file_name):
    return '_'.join(file_name.split('_')[:2]) + '_'


def _get_exercise_file_name_of_student(student_dir_path, exercise_file_name):
    for submission_root, submission_subdirs, submission_filenames in os.walk(student_dir_path):
        for file in submission_filenames:
            if _get_exercise_number_prefix(file) == _get_exercise_number_prefix(exercise_file_name):
                return file

    return False


def _run_all_student_assignments(student_dir_path, student_name):
    exercise_results = {}

    is_run_some_exe = False
    for exercise_file_name, inputs_to_exercise in ASSIGNMENTS_NAMES_AND_INPUTS.items():
        exercise_file_name_of_student = _get_exercise_file_name_of_student(student_dir_path, exercise_file_name)

        if exercise_file_name_of_student:
            exercise_path = student_dir_path + "/" + exercise_file_name_of_student
            try:
                is_run_some_exe = True
                _run_python_script(exercise_path, inputs_to_exercise)
                exercise_results[exercise_file_name] = True
            except:
                print("%s | Failed | %s" % (exercise_path.replace(' ', '\ '), sys.exc_info()[0]))
                exercise_results[exercise_file_name] = exercise_path.replace(' ', '\ ')
        else:
            add_comment_to_student(student_name, PYTHON_FILE_DOES_NOT_EXIST % exercise_file_name)
            exercise_results[exercise_file_name] = False

    if not is_run_some_exe:
        print("Failed to run files!")

    return exercise_results


def _run_python_script(python_script_path, inputs=None):
    with mock.patch('builtins.input', side_effect=inputs):
        exec(open(python_script_path).read())

