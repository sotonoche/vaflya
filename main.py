p = int(input('Введите простое число [p]: '))
q = int(input('Введите простое число [q]: '))

n = p * q
fi = (p-1)*(q-1)

e = int(input('Введите число [e]: '))

d = 0
i = 1

while True:
    if (e*i) % fi == 1:
        d = i
        break
    else:
        i += 1

print(f'\nE = ({e}, {n}) D = ({d}, {n}\n)')
s = int(input('Введите [s]: '))
t = pow(s, e, n)
print(f'Борис получает t, равное {t} и находит s, которое равно {pow(t, d, n)}')
