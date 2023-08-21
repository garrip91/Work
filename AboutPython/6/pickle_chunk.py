import pickle


chunk_size = 256
with open(file="random_million.pickle", mode="rb") as f:
    binary_data = bytearray()
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        binary_data.extend(chunk)
    nums = pickle.loads(binary_data)
print(f"{type(nums)}, {len(nums)}")
