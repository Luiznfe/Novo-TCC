from population import Population
import random
# local search
# 1 - recebe como entrada uma solução
# 2 - recupera as rotas (sem o deposito)
# 3 - realiza as operações (simultaneamente)
# 4 - compara a nova distancia com a anterior

def operations(s):
    # apenas as rotas são passadas para as operações
    routes = retrieve_routes(s)
    print(s)
    swap(routes)
    s.update_solution(routes)
    print(s)

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
    k = swap_k(len(a), len(b))
    # selecionando os elementos que serao trocados
    l = random.sample(range(0, len(a)), k)    
    m = random.sample(range(0, len(b)), k)    
    # realiza a troca 
    for i in range(len(l)):
        aux = a[l[i]]
        a[l[i]] = b[m[i]]
        b[m[i]] = aux
    
    
if __name__ == '__main__':
    p = Population(1)
    p.new_population('c0530.txt')
    operations(p.get_population()[0])
    