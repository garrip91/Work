import json
import pickle
import random
from time import perf_counter


nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]

start = perf_counter()
with open(file="random_million.json", mode="w", encoding="utf-8") as f:
    json.dump(nums, f)
print(f"json saved: {perf_counter() - start}")

start = perf_counter()
with open(file="random_million.pickle", mode="wb") as f:
    pickle.dump(nums, f)
print(f"pickle saved: {perf_counter() - start}")
