import keyword
name = input("Введите имя: ")
if (name.isidentifier() and not keyword.iskeyword(name)):
    print("Имя корректно")
else:
    print("Имя не корректно")
