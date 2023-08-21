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
    else:
        return None


print(num_translate("six"))
