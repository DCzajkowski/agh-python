try:
    n = int(input('Podaj liczbę:'))
except Exception:
    print('Podaj poprawną liczbę naturalną!')

if n <= 1:
    print('Liczba musi być większa od 1!')
    exit()

def tree(x, n):
    tree = ''

    for i in range(0, x):
        row = ''

        if x <= n:
            for l in range(0, n - x + 1):
                row += ' '

        for _ in range(0, x - i - 1):
            row += ' '

        for _ in range(0, (2 * i) - 1):
            row += 'x'

        tree += row + '\n'

    return tree.rstrip()


for x in range(1, n):
    print(tree(x + 2, n + 3), end='')
