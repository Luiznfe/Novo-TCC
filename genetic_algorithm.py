from solution import Solution
import random
import copy
import funcs

class GeneticAlgorithm:

    # calcula a função fitness
    def fitness_function(self, c_list, p):
        sp = 1.8
        c_size = len(c_list)
        fitness = list()
        for i in range(c_size):
            value = 2 - sp + 2 * (sp - 1) * ((i - 1)/(c_size - 1))
            fitness.append(value)
        p.sort_teste(c_list)
        p.set_fitness2(fitness, c_list)
        
        
    # a lista deve ser ordenada antes
    def tournamet_selection(self, p, c_list, k):
        # seleciona k elementso da minha lista
        selected = random.sample(c_list, k)
        # ordena a lista com base no fitness
        p.sort_teste(selected)
        # retorna o melhor elemento
        return selected.pop()


    # Order Crossover Operator (OX)
    # Acontece com uma alta probabilidade
    # Nesse cado devido a restrição da capacidade do caminhão, todas as rotas precisam ser refeitas.
    def crossover(self, p1, pop, cross_p):
        # p1 e p2 recebem a ordem de visitação dos pais
        c_p1 = list()
        c_p2 = list()
        # selecionando p2
        # k depende da probabilidade do crossover
        k = round(cross_p * len(pop.get_population()))
        while True:
            p2 = self.tournamet_selection(pop, pop.get_population(), k)
            if p2.get_id() != p1.get_id():
                break
        # recebe a ordem de visitação da solucao
        c_p1 = p1.get_sequence()
        c_p2 = p2.get_sequence()
        # sorteando os pontos de corte
        while True:
            c_point = random.sample(range(0, len(c_p1)), 2)
            c_point.sort()
            # para garantir uma minima parte herdada
            if c_point[0] != 0 and c_point[1] != len(c_p1) - 1: 
                break
        # uma base é criada para os filhos (copia parcial do pai)
        # off1
        self.get_offspring(c_p1, c_p2, c_point, pop)
        # off2
        self.get_offspring(c_p2, c_p1, c_point, pop)


    
    def get_offspring(self, p1, p2, c_point, pop):
        seq = list()
        seq_off = list()
        off_list = list()
        # seq recebe a sequencia de visitacao de p1
        seq = self.cross_sequence(p1, c_point)
        # seq_off recebe subconjunto de p2
        seq_off = self.inherited_seq(p2, c_point)
        # seq_off recebe a ordem de visitação de p1
        self.offspring_seq(seq_off, seq, c_point)
        # a lista com os clientes reais é recuperada (apenas os ids estavam sendo usados)
        aux = pop.get_population()[0]
        off_list = aux.get_new_client_list(seq_off)
        # uma nova solução "filho" é criada e adicionada a populacao
        off = pop.new_solution(off_list)
        pop.add_offspring(off)
        # retorna o filho
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
        # o array então recebe a parte herada 
        for i in range(c_point[0], c_point[1] + 1):
            in_seq[i] = p2[i]
        return in_seq
    
    # o filho recebe a parte herada do p1
    def offspring_seq(self, in_seq, new_seq, c_point):
        # remove os itens repetidos da lista
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

    # Mutação
    # Ainda preciso verificar
    # uma inversão é feita em uma faixa de tamanho proporcional PMUT
    def mutation(self, s , PMUT, prob_s):
        funcs.inversion(s, prob_s)

    # Seleciona os sobreviventes da população
    # 5% elitismo
    def survivior_selection(self, pop, pop_size):
        # juntar as duas listas (filhos e população atual)
        merged_list = pop.merge()
        # calcula o fitness da nova lista
        self.fitness_function(merged_list, pop)
        temp_list = list()
        # 5 % da população escolhida por elitismo
        e_size = round(0.05 * pop_size)
        for i in range(e_size):
            temp_list.append(merged_list.pop())
        # 80% tournament selection / # k = 10% da populção (quantidades de amostras comparadas)
        t_size = round(0.8 * pop_size)
        k = round(len(merged_list) * 0.1)
        for i in range(t_size):
            c = self.tournamet_selection(pop, merged_list, k)
            merged_list.remove(c)
            temp_list.append(c)
        # 15% random / ou até completar a lista
        while len(temp_list) != len(pop.get_population()):
            p = random.choice(merged_list)
            merged_list.remove(p)
            temp_list.append(p)
        pop.set_population(temp_list)


        
        


        

