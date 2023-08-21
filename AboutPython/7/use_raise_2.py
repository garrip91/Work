class CalcError(Exception):

    pass


def do_calc(f_path):
    f = open(file=f_path, mode="a", encoding="utf-8")
    try:
        x = float(input("Enter X val:\n"))
        y = float(input("Enter Y val:\n"))
        result = x / y
    except ValueError as e:
        print(f"Wrong val: {e}")
        raise CalcError
    except ZeroDivisionError:
        print("Fault: Zero division")
        raise CalcError
    else:
        f.write(f"{x} / {y} = {result}\n")
    finally:
        f.close()


if __name__ == "__main__":
    f_path = "calc_log.txt"
    try:
        do_calc(f_path)
    except CalcError:
        print("Calc fail")
        exit(1)
    except Exception as e:
        print(f"global error: {e}")
        exit(2)
