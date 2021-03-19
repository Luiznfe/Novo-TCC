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
        # sorteando os pontos de corte
        seq_p1 = []
        seq_p2 = []
        seq_p1 = parents[0].get_sequence()
        seq_p2 = parents[1].get_sequence()
        print(seq_p1)

        





    