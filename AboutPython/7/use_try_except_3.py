f_path = __file__
try:
    with open(file=f_path, mode="r", encoding="utf-8") as f:
        content = f.read()
except Exception as e:
    print(f"global error: {e}")
else:
    print(content)
