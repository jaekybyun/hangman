#[python_ex286.py]
#http://tinyurl.com/zy7pr4l

import re

line = "I love $"

m = re.findall("\\$", line, re.IGNORECASE)

print(m)