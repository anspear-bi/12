sentence = input("Введите предложение: ")
words = sentence.split()
first_word = words[0]
result = [w for w in words[1:] if len(set(w)) == len(w)]
print("Подходящие слова:", " ".join(result))
