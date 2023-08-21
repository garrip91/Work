import os
import shutil


to_remove_dir_name = "second_dir"
if os.path.exists(to_remove_dir_name):
    shutil.rmtree(to_remove_dir_name)
