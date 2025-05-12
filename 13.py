def is_lucky(ticket):
    n = len(ticket)
    if n % 2 != 0:
        return False
    half = n // 2
    s1 = sum(int(x) for x in ticket[:half])
    s2 = sum(int(x) for x in ticket[half:])
    return s1 == s2

count = 0
while True:
    ticket = input("Введите номер билета: ")
    count += 1
    if is_lucky(ticket):
        print("Порядковый номер счастливого билета:", count)
        break
