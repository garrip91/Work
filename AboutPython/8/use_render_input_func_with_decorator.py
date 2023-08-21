def p_wrapper(func):
    print(func)

    def tag_wrapper(*args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)
        markup = func(*args, **kwargs)
        print(markup)
        return markup

    return tag_wrapper


@p_wrapper
def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}" />'


username_f = render_input("username")
#print(username_f)
print(render_input)
