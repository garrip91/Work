import sys


price = sys.argv[1]

with open(file="bakery.csv", mode="a", encoding="utf-8") as f:
    f.write(price + "\n")
