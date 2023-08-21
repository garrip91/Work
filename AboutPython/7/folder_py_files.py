import os


# folder = r"/home/garrip91/Programming"
# py_files = [item for item in os.listdir(folder) if item.lower().endswith(".py")]
# py_files = [os.path.join(folder, item) for item in os.listdir(folder) if item.lower().endswith(".py")]
# print(py_files)

folder = r"/home/garrip91/Programming/GitHub/Work/venv/lib/python3.10/site-packages/bs4"
bs4_dirs = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
print(bs4_dirs)
