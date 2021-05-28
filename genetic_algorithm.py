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
        p.sort_d(c_list)
        p.set_fitness2(fitness, c_list)
        
        
    # a lista deve ser ordenada antes
    # seleção por torneio
    def tournamet_selection(self, p, c_list, k):
        # seleciona k elementso da minha lista
        selected = random.sample(c_list, k)
        # ordena a lista com base no fitness
        p.sort_f(selected)
        # retorna o melhor elemento
        return selected.pop()


    # Order Crossover Operator (OX)
    # Acontece com uma alta probabilidade
    # Nesse cado devido a restrição da capacidade do caminhão, todas as rotas precisam ser refeitas.
    def crossover(self, p1, pop, cross_p):
        # selecionando p2
        # k depende da probabilidade do crossover
        k = round(cross_p * len(pop.get_population()))
        while True:
            p2 = self.tournamet_selection(pop, pop.get_population(), k)
            if p2.get_id() != p1.get_id():
                break
        # recebe a ordem de visitação da solucao
        c_p1 = list()
        c_p2 = list()
        c_p1 = p1.id_list()
        c_p2 = p2.id_list()
        # sorteando os pontos de corte
        while True:
            c_point = random.sample(range(0, len(c_p1)), 2)
            c_point.sort()
            # para garantir uma minima parte herdada
            if c_point[0] != 0 and c_point[1] != len(c_p1) - 1: 
                break
        # dois novos filhos são gerados
        a = self.new_offspring(c_p1, c_p2, c_point, pop, p2)        
        self.new_offspring(c_p2, c_p1, c_point, pop, p1)


    
    def new_offspring(self, p1, p2, c_point, pop, p):
        seq = list()
        off_ids = list()
        off_list = list()
        # seq recebe a sequencia de visitacao de p1 (apenas ids, facilita a operação)
        seq = funcs.parent_seq(p1, c_point)
        # off_ids recebe subconjunto de p2
        off_ids = funcs.subset(p2, c_point)
        # off_ids recebe a ordem de visitação de p1
        funcs.off_seq(off_ids, seq, c_point)
        # a lista com os clientes reais é recuperada (apenas os ids estavam sendo usados)
        off_list = p.retrieve_list(off_ids)
        off_list.insert(0, p.get_clientList()[0])   
        # uma nova solução "filho" é criada e adicionada a lista de filhos
        off = pop.new_solution(off_list)
        pop.add_offspring(off)
        # retorna o filho
        return off
    
    # Mutação
    # Ainda preciso verificar
    # uma inversão é feita em uma faixa de tamanho proporcional PMUT
    def mutation(self, s , p_mut):
        funcs.inversion(s, p_mut)

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
            a = merged_list.pop()
            temp_list.append(a)
    
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