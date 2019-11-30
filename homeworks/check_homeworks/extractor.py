import os
import zipfile

from homeworks.check_homeworks.comments import *
from homeworks.check_homeworks.config import NUMBER_OF_ASSIGNMENT
from homeworks.check_homeworks.students import add_comment_to_student, set_zip_file_name, user_have_zip_file


def remove_zip_extention(zip_file_name):
    return zip_file_name.split(".zip")[0]


def extract_zip_file(zip_file, path_where_to_extract, original_zip_file_name=None):
    try:
        my_zipfile = zipfile.ZipFile(zip_file, mode='r')
        my_zipfile.extractall(path_where_to_extract)
        my_zipfile.close()

        if original_zip_file_name and os.path.isdir(path_where_to_extract + '/' + remove_zip_extention(original_zip_file_name)):
            for root, subdirs, filenames in os.walk(path_where_to_extract + '/' + remove_zip_extention(original_zip_file_name)):
                for file in filenames:
                    os.rename(root + '/' + file, path_where_to_extract + '/' + file)

        return True
    except:
        print("ERROR: Can't extract zip file: [%s]!" % zip_file)
        return False


def extract_submissions(base_subdir):
    for root, subdirs, filenames in os.walk(base_subdir):

        for subdir in sorted(subdirs):
            if not subdir.startswith('__'):
                current_student_name = subdir.split('_')[0]

                submission_dir_wrapper = base_subdir + '/' + subdir
                for submission_root, submission_subdirs, submission_filenames in os.walk(submission_dir_wrapper):

                    good_submission_filenames = [f for f in submission_filenames if f.endswith('.zip') and f.startswith("Ex%s_%s" % (NUMBER_OF_ASSIGNMENT, current_student_name.replace(' ', '_')))]
                    bad_submission_filenames = [f for f in submission_filenames if not f.endswith('.zip') or not f.startswith("Ex%s_%s" % (NUMBER_OF_ASSIGNMENT, current_student_name.replace(' ', '_')))]

                    if not len(submission_filenames) == 1:
                        add_comment_to_student(current_student_name, SHOULD_BE_SUBMITTED_ONLY_1_ZIP_FILE)
                    if len(bad_submission_filenames) > 0:
                        add_comment_to_student(current_student_name, WRONG_ZIP_FILE_FORMAT % bad_submission_filenames[0])

                    for file in good_submission_filenames:
                        extract_student_zip_assignment(base_subdir, current_student_name, file, submission_dir_wrapper)

                    if len(good_submission_filenames) == 0 and len(bad_submission_filenames) > 0:
                        for file in bad_submission_filenames:
                            if file.endswith('.zip'):
                                extract_student_zip_assignment(base_subdir, current_student_name, file, submission_dir_wrapper)


def extract_student_zip_assignment(base_subdir, current_student_name, file, submission_dir_wrapper):
    old_zip_file = submission_dir_wrapper + '/' + file
    # new_zip_file = base_subdir + '/' + file
    set_zip_file_name(current_student_name, file)
    new_zip_file = base_subdir + '/' + current_student_name + '.zip'
    os.rename(old_zip_file, new_zip_file)
    # print("Moved %s to %s" % (old_zip_file, new_zip_file))
    # print("About to rm: %s" % submission_dir_wrapper)
    try:
        os.rmdir(submission_dir_wrapper)
    except:
        print('ERROR:: can`t remove dir. In [%s] directory there is more then 1 zip file!' % submission_dir_wrapper)
    # print("About to extract zip file and remove it")
    if extract_zip_file(new_zip_file, remove_zip_extention(new_zip_file), file):
        os.remove(new_zip_file)
    else:
        add_comment_to_student(current_student_name, CANT_EXTRACT_ZIP_FILE)
