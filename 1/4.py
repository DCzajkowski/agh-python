try:
    n = int(input('Podaj liczbę:'))
except Exception:
    print('Podaj poprawną liczbę naturalną!')

if n >= 2:
    for i in range(1, n):
        for j in range(1, i + 2):
            for k in range(1, j + 1):
                print('x', end='')
            print()
else:
    print('Liczba musi być większa od 2!')
