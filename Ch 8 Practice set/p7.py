def rem(a, word):
    n = []

    for item in a:
        if not(item == word):
            n.append(item.strip(word))
    return n

a = ["amit", "vishnu", "aman", "an"]
print(rem(a, "an"))