from collections import OrderedDict

n = int(input())

dictionary = {}

for _ in range(n):
    word, meaning = input().split()
    dictionary[word] = meaning

sentence = input().strip()

words = sentence.split()

translated_words = [dictionary.get(word, word) for word in words]

translated_sentence = ' '.join(translated_words)

print(translated_sentence)
