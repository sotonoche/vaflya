p = int(input('Введите простое число [p]: '))
q = int(input('Введите простое число [q]: '))

n = p * q
fi = (p-1)*(q-1)

e = int(input('Введите число [e]: '))

D = 0
i = 1


"""
Поиск числа D
"""
while True:
    if not (e*i) % fi == 1:
        i += 1
    else:
        D = i
        break
        
print(f'\nE = ({e}, {n}) D = ({D}, {n}\n)')
s = int(input('Введите [s]: '))
t = pow(s, e, n)
print(f'Борис получает t, равное {t} и находит s, которое равно {pow(t, D, n)}')
