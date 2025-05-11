text = input("Введите текст: ")
max = 0
current_count = 0
for char in text:
    if char.isspace():
        current_count += 1
        max = max(max, current_count)
    else:
        current_count = 0
print("Максимальное количество последовательных пробелов:", max)
