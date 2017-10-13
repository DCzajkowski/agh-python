from math import sqrt

def end():
    print('Podana liczba jest niepoprawna')
    exit()

def validate(n):
    try:
        n = float(n)
    except Exception:
        end()

    if n < 0:
        end()

a = input('Podaj a: ')
validate(a)

b = input('Podaj b: ')
validate(b)

c = input('Podaj c: ')
validate(c)

if a < b + c or b < a + c or c < a + b: print('Niepoprawne liczby'), exit()

p = (a + b + c) / 2
print('Pole to:', sqrt(p * (p - a) * (p - b) * (p - c)))
