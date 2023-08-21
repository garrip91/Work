def do_calc(f_path):
    f = open(file=f_path, mode="a", encoding="utf-8")
    try:
        x = float(input("Enter x value:\n"))
        y = float(input("Enter y value:\n"))
    except ValueError as e:
        print(f"wrong val: {e}")
    else:
        result = x / y
        f.write(f"{x} / {y} = {result}\n")
    print("Closing file!")
    f.close()


if __name__ == "__main__":
    f_path = "calc_log.txt"
    try:
        do_calc(f_path)
    except ZeroDivisionError:
        print("Fault: Zero divizion")
    except Exception as e:
        print(f"global error: {e}")
