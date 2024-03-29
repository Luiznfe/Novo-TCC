import random
import numpy as np
import copy

# retorna uma nova sequencia de acordo com os pontos de corte
def parent_seq(p1, c_point):
    # começa do segundo ponto de corte e vai até o primeiro
    new_seq = []
    i = c_point[1] + 1
    while True:
        if i == len(p1):
            i = 0
        if i == c_point[1]:
            new_seq.append(p1[i])
            break
        new_seq.append(p1[i])
        i += 1
    return new_seq

# cria uma nova lista contendo um subconjunto de p2
def subset(p2, c_point):
    in_seq = []
    # o array é inicializado com X
    for i in range(len(p2)):
        in_seq.append('X')
    # o array então recebe o subconjunto 
    for i in range(c_point[0], c_point[1] + 1):
        in_seq[i] = p2[i]
    return in_seq

# in_seq recebe os itens restantes baseados a ordem de visitação
# de new_seq
def off_seq(in_seq, new_seq, c_point):
    # remove os itens repetidos da lista
    remove_duplicates(in_seq, new_seq)
    i = c_point[1] + 1
    while True:
        if len(new_seq) == 0:
            break
        if i == len(in_seq):
            i = 0
        in_seq[i] = new_seq.pop(0)
        i += 1
        # print('off', in_seq)

# remove os valores repetidos de duas listas
def remove_duplicates(in_seq, new_seq):
    for i in in_seq:
        if i in new_seq:
            new_seq.remove(i)


# um subconjunto é invertido 
def inversion(s, prob_s):
    arr = None
    try:
        # inicia um array com os id dos clientes
        arr = np.array(s.id_list())
        # decide o tamanho do intervalo com base pa probalidade de mutação
        size = round(prob_s * arr.size)
        # inverte o subconjunto escolhido
        aux = random.randint(0, arr.size - size)
        new_a = np.array(arr[aux :aux + size])
        arr[aux : aux + size] = new_a[::-1]
        # transforma em uma lista
        seq = list(arr)
        # atualiza a solução
        update_solution(s, arr)
    except Exception:
        print('mutation error')
    


def update_solution(s, seq):
    seq = s.retrieve_list(seq)
    s.reset_solution()
    s.set_client_list(seq)
    s.initial_solution()

if __name__ == '__main__':
    print('')
    


   # calcula o fitness de cada indivíduo da populacao
    # o calculo é feito com base na posição em que as solucoes estão e a quantidade 
    # ranqueamento linear
    # def fitness_function(self, pop, pop_size, off):
    #     # sp = selective pressure [1.0 , 2.0]
    #     sp = 1.8
    #     qt_solution = pop_size
    #     # o fitness é calculado
    #     fitness = list()
    #     for i in range(qt_solution):
    #         value = 2 - sp + 2 * (sp - 1) * ((i - 1)/(qt_solution - 1))
    #         fitness.append(value)
    #     # a populacao é ordenada de forma (maior distância -> menor distância)
    #     pop.sort_pop(True, off)
    #     # o fitness calculado é atribuido a cada solucao da populacao
    #     pop.set_fitness(fitness, off)
    


    
    # Parents Selection
    # K-Way Tournament Selection
    # k é o número de indivíduos da população selecionados
    # def tournamet_selection(self, pop, k):
    #     dict_pop = {}
    #     candidate = []
    #     # um dicionário que relacina id com o fitness é utilizada para selecionar os pais
    #     dict_pop = pop.get_dic()
    #     # k amostras são selecionadas aleatoriamente dentro do dicionário
    #     # o dicionário é ordenado e o item com maior fitness é selecionado
    #     # uma solucao é escolhida
    #     candidate = random.sample(dict_pop.items(), k)
    #     candidate = sorted(candidate, key=lambda item: item[1]).pop()[0]
    #     # com base no id a solução selecionado é recuperada
    #     p = pop.get_item(candidate)
    #     # a solução selecionada é retornada
    #     return p 