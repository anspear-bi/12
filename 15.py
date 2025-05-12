def is_valid_number(num):
    return len(num) == 4 and num.isdigit() and len(set(num)) == 4

def bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

while True:
    secret_number = input("Ведущий вводит число: ")
    if is_valid_number(secret_number):
        break
    else:
        print("Число должно быть четырехзначным с неповторяющимися цифрами. Попробуйте снова.")
print("\n" * 25)

attempts = 10
for attempt in range(1, attempts + 1):
    while True:
        guess = input(f"Попытка #{attempt}: ")
        if is_valid_number(guess):
            break
        else:
            print("Число должно быть четырехзначным с неповторяющимися цифрами. Попробуйте снова.")

    bulls, cows = bulls_and_cows(secret_number, guess)
    print(f"Быков: {bulls} Коров: {cows}")

    if bulls == 4:
        print("Победа!")
        break
else:
    print("Проигрыш!")
