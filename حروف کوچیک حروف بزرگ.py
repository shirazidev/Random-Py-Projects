def apply(word):
    up = sum(1 for kocholo in word if kocholo.isupper())
    low = sum(1 for kocholo in word if kocholo.islower())

    if up > low:
        return word.upper()
    else:
        return word.lower()

vorodi = input()
result = apply(vorodi)
print(result)