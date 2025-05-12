words = input("Введите города через пробел: ").split()
players = ["Петя", "Вася"]
last_char = None
loser = None
for i, city in enumerate(words):
    if i > 0:
        if city[0].lower() != last_char:
            loser = players[i % 2]
            break
    last_char = city[-1].lower()
if loser:
    print(f"Проиграл {loser}")
else:
    winner = players[(len(words) - 1) % 2]
    print(f"Победил {winner}")
