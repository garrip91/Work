from pathlib import Path
import os
import time
import shutil


external_path = Path.cwd()
project_dir = "my_project"
templates_dir = "templates"

if not os.path.exists(os.path.join(external_path, project_dir, templates_dir)):
    os.chdir(project_dir)
    os.mkdir(templates_dir)
else:
    pass

used_roots = []
for item in os.listdir(external_path):
    if item == project_dir:
        path_to_needed_dir = os.path.join(external_path, item)
        for root_1, dirs_list_1, files_list_1 in os.walk(path_to_needed_dir):
            for dir_2 in dirs_list_1:
                for root_2, dirs_list_2, files_list_2 in os.walk(os.path.join(path_to_needed_dir, dir_2)):
                    if root_2 not in used_roots:
                        used_roots.append(root_2)
                        if templates_dir in dirs_list_2:
                            templates_dir_2 = os.path.join(root_2, templates_dir)
                            internal_dir = os.listdir(templates_dir_2)[0]
                            dir_in_templates_folder = os.path.join(templates_dir_2, internal_dir)
                            shutil.copytree(dir_in_templates_folder, os.path.join(external_path, project_dir, templates_dir, internal_dir))
                    else:
                        continue
