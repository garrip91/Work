def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}" />'


username_f = render_input("username")
print(username_f)
