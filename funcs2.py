from population import Population
import random
# local search
# 1 - recebe como entrada uma solução
# 2 - recupera as rotas (sem o deposito)
# 3 - realiza as operações (simultaneamente)
# 4 - compara a nova distancia com a anterior

# fontes http://www.decom.ufop.br/marcone/Publicacoes/PRVCES-ANPET2009.pdf

def operations(s):
    # apenas as rotas são passadas para as operações
    routes = retrieve_routes(s)
    # swap (uma quantidade de elementos é trocada entre rotas)
    s.print_routes()
    shift_2(routes)
    s.update_solution(routes)
    
   
    
# recupera as rotas 
def retrieve_routes(s):
    routes = []
    # recupera as rotas (apenas os ids)
    vehicle_l = s.get_vehicle_list()
    for r in vehicle_l:
        routes.append(r.route_ids())
    return routes

# definir a quantidade de elementos trocados entre rotas
def swap_k(a, b):
    k = 1
    if a >= b:
        k = round(b * 0.3)
    else:
        k = round(a * 0.3)
    if k < 1: 
        k = 1
    return k

# A QUANTIDE DE ROTAS ESCOLHIDAS PODE MUDAR ?
def swap(routes):
    # duas rotas são escolhidas 
    a, b = random.sample(routes, 2)
    # k = quantidade de elementos trocados
    # 30% da quantidade de elementos da menor rota
    k = swap_k(len(a), len(b))
    # selecionando os elementos que serao trocados
    l = random.sample(range(0, len(a)), k)    
    m = random.sample(range(0, len(b)), k)    
    # realiza a troca 
    for i in range(len(l)):
        aux = a[l[i]]
        a[l[i]] = b[m[i]]
        b[m[i]] = aux
        
    return 1

    
# troca de dois elementso consecutivos entre rotas 
def swap_2(routes):
    a, b = random.sample(routes, 2)
    # verifica se o tamanha das rotas é maior que 2
    # sorteia o index 
    index_a = random.randint(0, len(a) - 2)
    index_b = random.randint(0, len(b) - 2)
        
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
def shift(routes):
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
    index_a = random.randint(0, len(a) - 2)
    list_a = a[index_a], a[index_a + 1]
    # remove os elementos de a
    a.remove(list_a[0])
    a.remove(list_a[1])
    # adiciona em b
    b.extend(list_a)
    return 1
        
    
    
    
    
    
if __name__ == '__main__':
    p = Population(1)
    p.new_population('c0530.txt')
    operations(p.get_population()[0])
    