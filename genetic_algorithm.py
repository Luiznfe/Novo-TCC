import random
import copy

class GeneticAlgorithm:

    # calcula o fitness de cada indivíduo da populacao
    # o calculo é feito com base na posição em que as solucoes estão e a quantidade 
    # ranqueamento linear
    def fitness_function(self, pop):
        # sp = selective pressure [1.0 , 2.0]
        sp = 1.8
        qt_solution = len(pop.get_population())
        # a populacao é ordenada de forma (maior distância - menor distância) percorrida
        pop.reverse_sorted()
        # o fitness é calculado
        fitness = list()
        for i in range(qt_solution):
            value = 2 - sp + 2 * (sp - 1) * ((i - 1)/(qt_solution - 1))
            fitness.append(value)
        # o fitness calculado é atribuido a cada solucao da populacao
        pop.set_fitness(fitness)


    # Parents Selection
    # K-Way Tournament Selection
    # 2 pais são selecionados
    # k é o número de indivíduos da população selecionados
    def tournamet_selection(self, pop, k):
        dict_pop = {}
        candidate = []
        parents_id = []
        # um dicionário que relacina id com o fitness é utilizada para selecionar os pais
        dict_pop = pop.get_dic()
        # k amostras são selecionadas aleatoriamente dentro do dicionário
        # o dicionário é ordenado e o item com maior fitness é selecionado
        for i in range(2):
            candidate = random.sample(dict_pop.items(), k)
            candidate = sorted(candidate, key=lambda item: item[1]).pop()[0]
            parents_id.append(candidate)
            dict_pop.pop(candidate)
        parents = []
        # com base no id a solução selecionado é recuperada
        for i in range(2):
            parents.append(pop.get_item(parents_id[i]))
            
        return parents 

    # Order Crossover Operator (OX)
    # Nesse cado devido a restrição da capacidade do caminhão, todas as rotas precisam ser refeitas.
    def crossover(self, parents):
        seq_1 = list()
        seq_2 = list()
        seq_1 = parents[0].get_sequence()
        seq_2 = parents[1].get_sequence()
        # sorteando os pontos de corte
        while True:
            c_point = random.sample(range(0, len(seq_1)), 2)
            if 0 not in c_point and c_point[0] != c_point[1]: 
                break
        # pontos de corte ordenados
        print(seq_1)
        print('-'*20)
        print(seq_2)
        print('-'*20)
        new_seq_1 = self.new_sequence(seq_1, c_point)
        self.offsring(new_seq_1, seq_2, c_point)
        # para criar um novo descendente preciso de duas coisas, a sequencia de P1 e de P2 preparada para receber a sequencia
        
    
    def new_sequence(self, seq_1, c_point):
        new_seq = list()
        i = c_point[1] + 1
        while True:
            if i == len(seq_1):
                i = 0
            if i == c_point[0]:
                break
            new_seq.append(seq_1[i])
            i += 1
    
    def offsring(self, new_seq, seq_2, c_point):
        new_o = list()
        for i in range(len(seq_2)):
            new_o.append('X')
        
        print(new_o)
        for i in range(c_point[0], c_point[1]):
            new_o[i] = seq_2[i]
        
        print(new_o)
        i = c_point[1] + 1
        while True:
            if i == len(seq_2):
                i = 0
            if i == c_point[0]:
                break
            if new_seq[-1] not in new_o:
                new_o[i] = new_seq.pop(0)
            print(i)
            i += 1
        print(new_o)

    

        





    