import re


RE_DATE = re.compile(r"(?:\d{2}[./-]){2}\d{4}")

txt = "Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. " \
      "Надеемся, что 24-01-2021 будет без ветра."

print(RE_DATE.findall(txt))
