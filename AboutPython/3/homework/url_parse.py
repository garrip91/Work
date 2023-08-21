def url_parse(url):
    _t_protocol, _, domain, *resource_address = url.strip("/").split("/")
    t_protocol = _t_protocol[:-1]
    return t_protocol, domain, resource_address


print(url_parse("https://gbcdn.mrgcdn.ru/uploads/asset/3836207/attachment/18a9bab017ed71a4fbd6c0b7efc1c618.pdf"))
