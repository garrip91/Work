f_path = "calc_log.txt"
f = open(file=f_path, mode="a", encoding="utf-8")
try:
    x = float(input("Enter x value:\n"))
    y = float(input("Enter y value:\n"))
except ValueError as e:
    print(f"wrong val: {e}")
else:
    result = x / y
    f.write(f"{x} / {y} = {result}\n")
f.close()
