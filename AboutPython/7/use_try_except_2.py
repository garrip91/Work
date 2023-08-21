f_path = "new_one.txt"
try:
    with open(file=f_path, mode="r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except Exception as e:
    print(f"global error: {e}")
except (FileNotFoundError, EOFError) as e:
    print(f"concrete error: {e}")
