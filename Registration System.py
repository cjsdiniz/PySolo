try:
    name = input()
    # your code goes here
    if len(name) < 4:
        raise NameError
    print("Account Created")

except NameError:
    print("Invalid Name")
