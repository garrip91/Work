"""
Task 2

*(вместо 1). Написать регулярное выражение для парсинга файла логов веб-сервера из ДЗ 6 урока nginx.txt
для получения информации вида:
(<remote_addr>,
<request_datetime>,
<request_type>,
<requested_resource>,
<response_code>,
<response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ("188.138.60.101", "17/May/2015:08:05:49 +0000", "GET", "/downloads/product_2", "304", "0")
"""


import re
import requests


PAD = re.compile(r"((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - "
                 r"(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) "
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')

url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
content = requests.get(url=url).text
for arg in PAD.findall(content):
    addr, datetime, r_type, resource, code, size = arg
    print(addr, datetime, r_type, resource, code, size)
