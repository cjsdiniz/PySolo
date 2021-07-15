import re
pattern = r"[1|8|9][0-9]{7}$"
stg = input()
match = re.search(pattern, stg)
if match:
    print("Valid")
else:
    print("Invalid")
stg = input()
match = re.search(pattern, stg)
if match:
    print("Valid")
else:
    print("Invalid")
