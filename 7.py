sentence = input("Введите предложение: ")
words = sentence.split()
min_len = min(len(w) for w in words)
print("Длина самого короткого слова:", min_len)
