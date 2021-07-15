
import re
print("\n*** Regular Expressions ***")
###
# The re.match function can be used to determine whether
# it matches at the beginning of a string
###

pattern = r"spam"

print("\n* #1 *")
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

print("\n* #2 *")

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))
# print(re.finditer(pattern, "eggspamsausagespam"))

print("\n* #3 *")

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

print("\n* #4 *")

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

print(re.sub("Ana", "Carlos", "O meu nome é Ana. Olá Ana."))

print("\n** Simple Metacharacters **")
print("\n#1")

pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
else:
    print("No match")
if re.match(pattern, "gray"):
    print("Match 2")
else:
    print("No match")
if re.match(pattern, "blue"):
    print("Match 3")
else:
    print("No match")

print("\n* #2 *")
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")
else:
    print("No match")
if re.match(pattern, "gray"):
    print("Match 2")
else:
    print("No match")
if re.match(pattern, "stingray"):
    print("Match 3")
else:
    print("No match")
print("\n** Character Classes **")
print("\n* #1 *")

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

print("\n* #2 *")

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

print("\n* #3 *")

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

print("\n** More Metacharacters **")
print("\n* #1 *")

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")


print("\n* #2 *")
pattern = r"g+"
if re.match(pattern, "g"):
    print("Match 1")
if re.match(pattern, "gggggggggggggg"):
    print("Match 2")
if re.match(pattern, "abc"):
    print("Match 3")

print("\n* #3 *")
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
    print("Match 1")
else:
    print(0)
if re.match(pattern, "icecream"):
    print("Match 2")
else:
    print(0)
if re.match(pattern, "sausages"):
    print("Match 3")
else:
    print(0)
if re.match(pattern, "ice--ice"):
    print("Match 4")
else:
    print(0)

print("\n* #4 *")

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")

print("\n** Groups **")
print("\n* #1 *")

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())


print("\n* #2 *")

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

print("\n* #3 *")

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1")

match = re.match(pattern, "grey")
if match:
    print("Match 2")

match = re.match(pattern, "griy")
if match:
    print("Match 3")


print("\n** Special Sequences **")
print("\n* #1 *")

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

print("\n* #2 *")

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

print("\n* #3 *")

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print("Match 3")


print("\n** Email Extraction **")
print("\n* #1 *")

# Ex: Our goal is to extract the substring "info@sololearn.com"
str = "Please contact info@sololearn.com for assistance"
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.search(pattern, str)
if match:
    print(match.group())
