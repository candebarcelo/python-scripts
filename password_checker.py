import re

# password can be made up of lower-case letters, upper-case letters, numbers and these #$%@ characters.
# it must be at least 8 characters long and end in a number.
pattern = re.compile(r"^[A-Za-z0-9\$%#@]{7,}\d$")
password = "hoGSFlahola$#@14%2"

pass_check = pattern.search(password)
print(pass_check)
