import random
lista = [1, 2, 3, 4, 5, 6]
lista2 = ['a', 'b', 'c', 'd', 'e', 'f']
filho = []
a = []
point = 2
point2 = 4
i = point2 + 1
while True:
    if i == len(lista):
        i = 0
    if i == point:
        break
    a.append(lista[i])
    i += 1

print('lista ',lista )
print('lista - a ',a )

for i in range(len(lista)):
    filho.append('X')

for i in range(2, 4+1):
    filho[i] = lista2[i]
print(filho)

i = 4+1
j = 2
while True:
    if i == len(lista):
        i = 0
    if i == j:
        break
    f = a[-1]
    if f not in filho:
        filho[i] = a.pop(0)
    i += 1
print(filho)

