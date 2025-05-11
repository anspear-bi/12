import string

text = input("Введите текст: ").lower()
letters = set()
for char in text:
    if char.isalpha():
        letters.add(char)
print("Количество различных букв в тексте:", len(letters))
