text = input("Введите текст: ")
max = 0
current_count = 1
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        current_count += 1
        max = max(max, current_count)
    else:
        current_count = 1
max = max(max, current_count)
print("Максимальное количество последовательных одинаковых символов:", max)
