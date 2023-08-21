import os


main_dir_name = "my_project"
needed_subdirs = ["settings", "mainapp", "adminapp", "authapp"]
if not os.path.exists(main_dir_name):
    os.mkdir(main_dir_name)
    os.chdir(main_dir_name)
    print(os.getcwd())
    for needed_subdir in needed_subdirs:
        if not os.path.exists(needed_subdir):
            os.mkdir(needed_subdir)

