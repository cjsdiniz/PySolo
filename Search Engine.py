
text = input("Texto: ")
word = input("Palavra: ")


def search(text, word):
    words = text.split(" ")
    for w in words:
        if w == word:
            return "Word found"
            break
    return "Word not found"


print(search(text, word))
