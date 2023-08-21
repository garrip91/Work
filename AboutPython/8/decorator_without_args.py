def simple_cache(func):
    cache = {}

    def wrapper(*args):
        nonlocal cache
        key = str(*args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    
    return wrapper


@simple_cache
def render_input(field):
    print(f"call render_input('{field}')")
    return f'<input id="id_{field}" type="text" name="{field}" />'


username_f = render_input("username")
print(username_f)
password_f = render_input("password")
print(password_f)
username_f_2 = render_input("username")
print(username_f_2)
