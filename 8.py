sentence = input("Введите предложение: ")
words = sentence.split()
words_sorted = sorted(words, key=len)
print(" ".join(words_sorted))
