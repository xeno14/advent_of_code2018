import sys
import re
import datetime

with open("input/")

def parse_line(line):
    matched = re.search(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] .*#(\d+) (.*)$", line)
    (yyyy, mm, dd, h, m, guard, action) = matched.groups()
    return {
        "time": datetime.datetime(int(yyyy), int(mm), int(dd), int(h), int(m)),
        "guard": guard,
        "action": action,
    }

print(parse_line(a[0]))