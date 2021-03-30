import random
import numpy as np
import copy

# seleciona um subconjunto da lista de clientes e o embaralha
def scramble(s):
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

def swap(s):
    # pegar a sequencia da solução
    arr = s.get_sequence()
    values = random.sample(range(0, len(arr)), 2)
    aux = arr[values[0]]
    arr[values[0]] = arr[values[1]]
    arr[values[1]] = aux
    update_solution(s, arr)

def swap_2(s):
    arr = np.array(s.get_sequence())
    values = random.sample(range(0, len(arr)), 4)
    aux = arr[values[0]]
    arr[values[0]] = arr[values[1]]
    arr[values[1]] = aux
    aux = arr[values[2]]
    arr[values[2]] = arr[values[3]]
    arr[values[3]] = aux
    seq = list(arr)
    update_solution(s, seq)

# um subconjunto é invertido 
def inversion(s, prob_s):
    arr = None
    try:
        arr = np.array(s.get_sequence())
        size = round(prob_s * arr.size)
        print(arr)
        aux = random.randint(0, arr.size - size)
        new_a = np.array(arr[aux :aux + size])
        arr[aux : aux + size] = new_a[::-1]
        print(f'{aux}, {aux + size}')
        print('mutation ',arr)
        seq = list(arr)
        update_solution(s, arr)
    except Exception:
        print('mutation error')

def local_search(s):
    c_aux = s.get_clientList()
    aux_dist = s.get_distance()
    count = 0
    while True:
        # funcs.scramble(a)
        swap(s)
        swap_2(s)
        # funcs.inversion(a)
        if s.get_distance() < aux_dist :
            break
        if count > 30:
            s.reset_solution()
            s.set_client_list(c_aux)
            s.initial_solution()
        count += 1

def update_solution(s, seq):
    seq = s.get_new_client_list(seq)
    s.reset_solution()
    s.set_client_list(seq)
    s.initial_solution()

if __name__ == '__main__':
    inversion(2, 3)