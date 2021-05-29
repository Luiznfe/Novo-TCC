from population import Population
import random
from plot import Plot
# local search
# 1 - recebe como entrada uma solução
# 2 - recupera as rotas (sem o deposito)
# 3 - realiza as operações (simultaneamente)
# 4 - compara a nova distancia com a anterior

# fontes http://www.decom.ufop.br/marcone/Publicacoes/PRVCES-ANPET2009.pdf


# 3.3Méto dodeDescida/Subida Randômica
def local_search(s, iterMax):
    iter = 0
    op = 0
    while iter < iterMax:
        iter += 1
        op = operations(s)
        if op == 1:
            iter = 0
            
def ls(s):
    while True:
        o = operation(s)
        if o == 1:
            break

def operations(s):
    routes = retrieve_routes(s)
    swap_1(routes)
    op = s.update_solution(routes)
    return op

def operation(s):
    routes = retrieve_routes(s)
    swap_struc(s, routes)
    return 1

# recupera as rotas sem o deposito
def retrieve_routes(s):
    routes = []
    # recupera as rotas (apenas os ids)
    vehicle_l = s.get_vehicle_list()
    for r in vehicle_l:
        routes.append(r.route_ids())
    return routes

def swap_struc(s, routes):
    a, b = random.sample(routes, 2)
    for i in range(len(a)):
        for j in range(len(b)):
            swap_test(a, b, i , j)
            o = s.update_solution(routes)
            if o == 1:
                break
        else:
            continue
        break
    return 1
            
def swap_test(a, b, i, j):
    aux = a[i]
    a[i] = b[j]
    b[j] = aux
    return 1

# um elemento de a é trocado com outro elemento de b
def swap_1(routes):
    # duas rotas são escolhidas 
    a, b = random.sample(routes, 2)
    # k = quantidade de elementos trocados
    k = 1
    # selecionando os elementos que serao trocados
    l = random.sample(range(0, len(a)), k)    
    m = random.sample(range(0, len(b)), k)    
    # realiza a troca 
    for i in range(len(l)):
        aux = a[l[i]]
        a[l[i]] = b[m[i]]
        b[m[i]] = aux
        
    return 1

# troca dois indivíduos dentro da mesma rota
def swap_3(routes):
    try:
        # seleciona uma rota
        a = random.choice(routes)
        # seleciona o index dos dois indivíduos trocados
        f_index, s_index = random.sample(range(0, len(a)), 2)
        # realiza a troca
        aux = a[f_index]
        a[f_index] = a[s_index]
        a[s_index] = aux
        return 1
    except:
        return 0
    

# troca um elemento de posição dentro de uma rota
def shift_3(routes):
    # escolhe a rota
    try:
        a = random.choice(routes)
        # escolhe o index (de onde será retirado e onde será colocado)
        r_index, i_index = random.sample(range(0, len(a)), 2)
        # remove o elemento
        ele = a.pop(r_index)
        # reincere 
        a.insert(i_index, ele)
        return 1
    except :
        return 0

    
# troca de dois elementso consecutivos entre rotas 
def swap_2(routes):
    a, b = random.sample(routes, 2)
    # verifica se o tamanha das rotas é maior que 2
    # sorteia o index 
    try:
        index_a = random.randint(0, len(a) - 2)
        index_b = random.randint(0, len(b) - 2)
    except :
        return 0
        
    list_a = a[index_a], a[index_a + 1]
    list_b = b[index_b], b[index_b + 1]
        
    #  a recebe os elementos de b
    a[index_a] = list_b[0]
    a[index_a + 1] = list_b[1]
        
    b[index_b] = list_a[0]
    b[index_b + 1] = list_a[1]
        
    return 1
    
        
# um cliente e transferido de uma rota para outra
# um cliente de a é movido para b
def shift_1(routes):
    a, b = random.sample(routes, 2)        
    # escolhe o cliente
    c = random.choice(a)
    # remove c de a 
    a.remove(c)
    # adiciona c em b
    b.append(c)
    return 1

# move dois clientes consecutivos de a para b
def shift_2(routes):
    a, b = random.sample(routes, 2)
    # escolha dos clientes
    try:
        index_a = random.randint(0, len(a) - 2)
    except:
        return 0
    list_a = a[index_a], a[index_a + 1]
    # remove os elementos de a
    a.remove(list_a[0])
    a.remove(list_a[1])
    # adiciona em b
    b.extend(list_a)
    return 1
             
    
if __name__ == '__main__':
    
    p = Population(10)
    p.new_population_2('c2.txt')
    i = p.get_population()[0]
    
    local_search(i, 100)
    print(p.get_population()[0])
    
    
    
        