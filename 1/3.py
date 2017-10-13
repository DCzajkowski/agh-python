from random import randint

x = random.randint(0, 9)
guessed == False

while guessed == False:
    n = input('Podaj liczbę:')

    if n == x:
        print('Dobrze!')
        guessed = True

    if n > x:
        print('Liczba zbyt duża')
    else:
        print('Liczba zbyt mała')

