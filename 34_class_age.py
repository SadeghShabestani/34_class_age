import termcolor2
from tamrin.birthday.date import Date

print(termcolor2.colored("Enter Date Birthday", color="blue"))
d1 = int(input("Enter Day: "))
m1 = int(input("Enter Month: "))
y1 = int(input("Enter Year: "))

print(termcolor2.colored("Enter Date Today", color="blue"))
date = Date()

day = d1 - date.date["d2"]
month = m1 - date.date["m2"]
year = y1 - date.date["y2"]

if day < 1:
    day += 30
    month -= 1

if month < 1:
    month += 12
    year -= 1

print(f"Age: {year} : {month} : {day}")
