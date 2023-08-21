def p_wrapper(func):
    def tag_wrapper(*args, **kwargs):
        markup = func(*args, **kwargs)
        return f"<p>{markup}</p>"
    
    return tag_wrapper


@p_wrapper
def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}" />'


username_f = render_input("username")
print(username_f)
