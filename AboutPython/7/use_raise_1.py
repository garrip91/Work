def do_calc(f_path):
    f = open(file=f_path, mode="a", encoding="utf-8")
    try:
        x = float(input("Enter X val:\n"))
        y = float(input("Enter Y val:\n"))
    except ValueError as e:
        print(f"Wrong val: {e}")
        raise ValueError
    else:
        result = x / y
        f.write(f"{x} / {y} = {result}\n")
    finally:
        f.close()


if __name__ == "__main__":
    f_path = "calc_log.txt"
    try:
        do_calc(f_path)
    except ZeroDivisionError:
        print("Fault: Zero division")
        exit(1)
    except Exception as e:
        print(f"global error: {e}")
        exit(2)
