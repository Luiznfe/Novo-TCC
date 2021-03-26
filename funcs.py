import random
import numpy as np
import copy

# seleciona um subconjunto da lista de clientes e o embaralha
def scramble(s):
    # s = copy.deepcopy(a)
    # pegar a sequencia da solução
    arr = np.array(s.get_sequence())
    # sortear o intervalo, o intervalo tera um tamanho mínimo de 20% do tamanho da lista
    # Ou deixar aleatorio    
    while True:
        interval = random.sample(range(0, arr.size), 2)
        if abs(interval[0] - interval[1] > int(0.2 * arr.size)):
            break
    interval.sort()
    np.random.shuffle(arr[interval[0] : interval[1]])
    seq = list(arr)
    update_solution(s, seq)
    return s

def update_solution(s, seq):
    seq = s.get_new_client_list(seq)
    s.reset_solution()
    s.set_client_list(seq)
    s.initial_solution()

def swap(s):
    # pegar a sequencia da solução
    # arr = np.array(s.get_sequence())
    arr = s.get_sequence()
    values = random.sample(range(0, len(arr)), 2)
    aux = arr[values[0]]
    arr[values[0]] = arr[values[1]]
    arr[values[1]] = aux
    update_solution(s, arr)

# um subconjunto é invertido 
def inversion(s):
    arr = None
    try:
        arr = np.array(s.get_sequence())
   
        # sortear o intervalo, o intervalo tera um tamanho mínimo de 20% do tamanho da lista
        interval = list()
        while True:
            interval = random.sample(range(0, arr.size), 2)
            if abs(interval[0] - interval[1] > int(0.2 * arr.size)):
                break
        interval.sort()
        new_a = np.array(arr[interval[0]:interval[1]])
        arr[interval[0]:interval[1]] = new_a[::-1]
        seq = list(arr)
        update_solution(s, arr)
    except :
        print('erro em ',s)



    