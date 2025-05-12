def main():
    # Ввод подсказки и загаданного слова
    hint = input("Введите подсказку: ")
    word = input("Введите загаданное слово: ").lower()
    
    # Очистка экрана выводом 25 пустых строк
    print("\n" * 25)
    
    attempts = 10
    guessed_letters = set()
    
    def display_word():
        displayed = ""
        for ch in word:
            if ch in guessed_letters:
                displayed += ch
            else:
                displayed += "*"
        return displayed
    
    print(hint)
    print(display_word())
    
    while attempts > 0:
        choice = input("Буква или слово (0 - буква, 1 - слово)? ")
        
        if choice == "0":
            letter = input().lower()
            if letter in word:
                guessed_letters.add(letter)
            else:
                attempts -= 1
            current = display_word()
            print(current)
            if current == word:
                print("Победа!")
                return
        elif choice == "1":
            answer = input().lower()
            if answer == word:
                print("Победа!")
                return
            else:
                attempts -= 1
                print(display_word())
        else:
            print("Некорректный ввод, введите 0 или 1.")
    
    print("Проигрыш!")

if __name__ == "__main__":
    main()
