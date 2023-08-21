import json
import random


nums = [random.randint(0, 100) for _ in range(10)]

with open(file="nums_again.json", mode="w", encoding="utf-8") as f:
    json.dump(nums, f)

with open(file="nums_again.json", mode="r", encoding="utf-8") as f:
    json.load(f)
