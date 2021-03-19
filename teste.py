import random
lista = [1, 2, 3, 4, 5, 6]
a = []
point = 0
point2 = 5
i = point2 + 1
while True:
    if i == point:
        break
    if i == len(lista):
        i = 0
    a.append(lista[i])
    print(a)
    i += 1
    print(i)
print('lista ',lista )
print('lista - a ',a )