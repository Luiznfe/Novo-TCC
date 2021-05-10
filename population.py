from operator import attrgetter, itemgetter
from solution import Solution
from read import Read
import random
import copy

class Population:

    def __init__(self, size):
        self.pop = list()
        self.offspring = list()
        self.size = size
        self.last_id = size + 1


    # gera um população inicial com base to no tamanho passado
    # todas as soluções sao geradas de forma aleatória
    def new_population(self, path):
        r = Read(path)
        cap, c_list, adj_matrix = r.create_instance()
        for i in range(self.size):
            s = Solution(c_list, adj_matrix, cap, i)
            s.random_client_list()
            s.initial_solution()
            self.pop.append(s)

    # retorna a populacao
    def get_population(self):
        return self.pop
    
    def set_population(self, new_pop):
        self.pop = new_pop[:]

    def get_offsprings(self):
        return self.offspring
    
    # retorna o ultimo id que pode ser usado
    def get_last_id(self):
        return self.last_id

    # adiciona uma solução a populacao e incrementa o últmo id
    def add_offspring(self, new_p):
        self.offspring.append(new_p)
        self.last_id += 1

    # remove uma solução da lista de soluções
    def remove_solution(self, s_id):
        try:
            for a in self.pop:
                if a.get_id() == s_id:
                    self.pop.remove(a)
        except Exception:
            print('remove solution error')
    
    # embaralha populção
    def shuffle_pop(self):
        random.shuffle(self.pop)

    # ordena a populacao de forma reversa
    def sort_pop(self, arg, off):
        if off == 0:
            self.pop.sort(key=attrgetter('dist'), reverse=arg)
        else:
            self.offspring.sort(key=attrgetter('dist'), reverse=arg)
    
    def set_fitness2(self, fitness, aux_list):
        for i, s in enumerate(aux_list):
            s.set_fitness(fitness[i])

 
    # retorna uma solução com id_s
    def get_item(self, id_s):
        for s in self.pop:
            if s.get_id() == id_s:
                return s


    # da um print na solução
    def print_population(self):
        for s in self.pop:
            print(f'{s.get_id()}, {s.get_distance()}, {s.get_fitness()}')
            
    def print_offsprings(self):
        for s in self.offspring:
            print(f'{s.get_id()}, {s.get_distance()}, {s.get_fitness()}')

        
    # gera uma nova solução com base em uma lista de clientes  
    def new_solution(self, client_list):
        try:
            aux = self.pop[0]
            new_s = Solution(None, aux.get_adj_matrix(), aux.get_capacity(), self.last_id)
            new_s.set_client_list(client_list)
            new_s.initial_solution()
            return new_s
        except :
            print('offspring error')
    
    def print_fitness(self):
        for i in self.pop:
            print(f'{i.get_id()}, {i.get_fitness()}')
    
    # funde a população atual com os filhos
    def merge(self):
        merged_list = []
        merged_list = self.pop[:]
        for i in self.offspring:
            merged_list.append(i)
        # self.sort_teste(merged_list)
        self.offspring.clear()
        return merged_list

    
    def best_solution(self):
        aux = self.pop[:]
        self.sort_d(aux)
        print(aux[-1].get_distance())
        
    def sort_d(self, c_list):
        c_list.sort(key=attrgetter('dist'), reverse=True)
    
    def sort_f(self, list):
        list.sort(key=attrgetter('fitness'), reverse=True)
    
if __name__ == '__main__':

    p = Population(3)
    p.new_population('c0530.txt')

  

