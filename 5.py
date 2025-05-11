s1 = input("Первая строка: ")
s2 = input("Вторая строка: ")
s3 = input("Третья строка: ")
chars = set(s1 + s2 + s3)
result = [c for c in chars if (c in s1,) + (c in s2,) + (c in s3,).count(True) == 1]
print("Символы, встречающиеся только в одной строке:", ''.join(result))
