import re


# RE_DATE = re.compile(r"^(\d{2}\.){2}\d{4}$")
# RE_DATE = re.compile(r"^(\d{2}.){2}\d{4}$")
RE_DATE = re.compile(r"^(\d{2}[./-]){2}\d{4}$")

#print(RE_DATE)

# for date in ["23.01.2021", "23,01,2021", "23~01~2021"]:
    # assert RE_DATE.match(date), f"wrong date {date}"

print(RE_DATE.match(date))
