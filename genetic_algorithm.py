from solution import Solution
import random
import copy
import funcs

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
    # Acontece com uma alta probabilidade
    # Nesse cado devido a restrição da capacidade do caminhão, todas as rotas precisam ser refeitas.
    def crossover(self, parents, pop):
        # p1 e p2 recebem a ordem de visitação dos pais
        p1 = list()
        p2 = list()
        p1 = parents[0].get_sequence()
        p2 = parents[1].get_sequence()
        # sorteando os pontos de corte
        while True:
            c_point = random.sample(range(0, len(p1)), 2)
            c_point.sort()
            # para garantir uma minima parte herdada
            if c_point[0] != 0 and c_point[1] != len(p1) - 1: 
                break
        
        # uma base é criada para os filhos (copia parcial do pai)
        offsprings = list()
        offsprings.append(self.get_offspring(p1, p2, c_point, pop))
        offsprings.append(self.get_offspring(p2, p1, c_point, pop))


    
    def get_offspring(self, p1, p2, c_point, pop):
        seq = list()
        seq_off = list()
        off_list = list()
        # seq recebe a sequencia de visitacao de p1
        seq = self.cross_sequence(p1, c_point)
        # seq_off recebe a parte herdade de p2
        seq_off = self.inherited_seq(p2, c_point)
        # seq_off recebe a parte herdade de p1
        self.offspring_seq(seq_off, seq, c_point)
        # a lista com os clientes reais é recuperada 
        aux = pop.get_population()[0]
        off_list = aux.get_new_client_list(seq_off)
        # uma nova solução "filho" é criada e adicionada a populacao
        off = pop.new_solution(off_list)
        pop.add_solution(off)
        return off

        
    # retorna uma nova sequencia de acordo com os pontos de corte
    def cross_sequence(self, p1, c_point):
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
    
    # cria uma nova sequencia e aplica a parte herdada do pai2
    def inherited_seq(self, p2, c_point):
        in_seq = []
        # o array é inicializado com X
        for i in range(len(p2)):
            in_seq.append('X')
        # o array então rece a parte herada 
        for i in range(c_point[0], c_point[1] + 1):
            in_seq[i] = p2[i]
        return in_seq
    
    # o filho recebe a parte herada do p1
    def offspring_seq(self, in_seq, new_seq, c_point):
        self.remove_repeated(in_seq, new_seq)
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
    def remove_repeated(self, in_seq, new_seq):
        for i in in_seq:
            if i in new_seq:
                new_seq.remove(i)

    # Mutation
    def mutation(self, pop, prob):
  

        
       


                




            
        

    

        





    