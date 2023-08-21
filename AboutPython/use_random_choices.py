import random


lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
random_choices = random.choices(lst, k=5)
full = ''.join(random_choices)
result = f"{full[:-1]},{full[-1]}"
print(result)
