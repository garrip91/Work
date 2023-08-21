# valid_letters = {chr(sym_code) for sym_code in range(ord("а"), ord("я") + 1)}
# valid_letters.add("ё")
import re

RE_NAME = re.compile(r"^[А-ЯЁ] [а-яё]+$")

def name_is_valid(name):
    # if not name or set(name.lower()) - set(valid_letters):
        # return False
    # return name.istitle()
    return RE_NAME.match(name)


if __name__ == "__main__":
    while True:
        name = input("Введите имя:\n")
        if name_is_valid(name):
            break
    print(f"Пользователь: {name}")
