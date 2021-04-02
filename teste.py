from operator import attrgetter, itemgetter
class Point:

    def __init__(self, p1):
        self.p1 = p1
    
    def __repr__(self):
        return f'{self.p1}'
    

lista = []
p1 = Point(5)    
p2 = Point(4)    
p3 = Point(12)
lista.append(p1)    
lista.append(p2)    
lista.append(p3)

for i in lista:
    print(i)

sorted(lista, key=lambda item: item[2])


for i in lista:
    print(i, end=' ')

