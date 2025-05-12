sentence = input("Введите предложение: ")
words = sentence.split()
from collections import Counter
counter = Counter(words)
for word, cnt in counter.items():
    if cnt == 2:
        print("Слово, которое встречается дважды:", word)
        break
