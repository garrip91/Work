nums = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь"
}


def num_translate(num: str):

    if num in nums:
        return nums[num]
    elif num.isupper():
        return nums[num.lower()].upper()
    elif num.istitle():
        return nums[num.lower()].title()
    else:
        return None


print(num_translate("Six"))
