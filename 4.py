text = input("Введите текст: ")
from collections import Counter
counter = Counter(text)
for char, count in counter.items():
    if count == 3:
        print("Символ, встречающийся ровно три раза:", char)
        break
