import random
import shutil


for _ in range(3):
    with open(file=r"/home/garrip91/Programming/GitHub/Work/AboutPython/7/data/hello.txt", mode="r", encoding="utf-8") as src:
        with open(file=r"/home/garrip91/Programming/GitHub/Work/AboutPython/7/data/summary.txt", mode="a", encoding="utf-8") as dst:
            head_size = random.randrange(21)
            print(head_size, src.read(head_size))
            shutil.copyfileobj(src, dst)
