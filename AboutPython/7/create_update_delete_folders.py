import os


# dir_name = "sample_dir"
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)

# dir_path = os.path.join("data", "src")
# if not os.path.exists(dir_path):
#     # os.mkdir(dir_path)
#     os.makedirs(dir_path)

# dir_name = "first_dir"
# # new_dir_name = "first_new_dir"
# new_dir_name = "../first_out_dir"
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)

to_remove_dir_name = "second_dir"
if os.path.exists(to_remove_dir_name):
    # os.remove(to_remove_dir_name)
    os.rmdir(to_remove_dir_name)
