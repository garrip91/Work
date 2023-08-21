import json
import pickle
from time import perf_counter


start = perf_counter()
with open(file="random_million.json", mode="r", encoding="utf-8") as f:
    nums = json.load(f)
print(f"json loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}")

start = perf_counter()
with open(file="random_million.pickle", mode="rb") as f:
    nums = pickle.load(f)
print(f"pickle loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}")
