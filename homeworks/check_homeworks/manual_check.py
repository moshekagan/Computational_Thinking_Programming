import os
import sys

from homeworks.check_homeworks.check_homeworks import _run_python_script
from homeworks.check_homeworks.config import ASSIGNMENTS_NAMES_AND_INPUTS

dir_path = "/Users/moshekagan/Documents/idc/submitions/Exercise_1/Ynonn Habib/Ex1_Ynonn_Habib_805373"

for submission_root, submission_subdirs, submission_filenames in os.walk(dir_path):
    for file in submission_filenames:
        if file.endswith('.py'):
            exercise_path = submission_root + "/" + file
            try:
                if file in list(ASSIGNMENTS_NAMES_AND_INPUTS.keys()):
                    _run_python_script(exercise_path, ASSIGNMENTS_NAMES_AND_INPUTS[file])
                else:
                    _run_python_script(exercise_path)
                print("%s is working! :)" % file)
            except:
                print("%s is not working! :(" % file)


