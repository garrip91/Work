import os
from shutil import copyfile, copy, copy2


def show_stat(f_path):
    stat = os.stat(f_path)
    print("{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}".format(
        f_p=f_path,
        perm=oct(stat.st_mode),
        m_t=stat.st_mtime,
        a_t=stat.st_atime,
    ))


src = r"data/summary.txt"
show_stat(src)
show_stat(copyfile(src, r"new_data/summary_clone.txt"))
show_stat(copy(src, "new_data"))
show_stat(copy2(src, r"new_data/summary_clone_2.txt"))
