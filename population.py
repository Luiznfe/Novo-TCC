from operator import attrgetter, itemgetter
from solution import Solution
from read import Read
import copy
class Population:

    def __init__(self, size):
        self.pop = list()
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
    
    # retorna o ultimo id que pode ser usado
    def get_last_id(self):
        return self.last_id

    # adiciona uma solução a populacao e incrementa o últmo id
    def add_solution(self, new_p):
        self.pop.append(new_p)
        self.last_id += 1

    # ordena a populacao de forma reversa
    def reverse_sorted(self):
        self.pop.sort(key=attrgetter('dist'), reverse=True)

    # atribui o fitness a cada solução da populacao
    def set_fitness(self, fitness):
        for i, s in enumerate(self.pop):
            s.set_fitness(fitness[i])
    
    def get_dic(self):
        pop_dic = dict()
        for s in self.pop:
            pop_dic[s.get_id()] = s.get_fitness()
        return pop_dic
    
    def get_item(self, id_s):
        for s in self.pop:
            if s.get_id() == id_s:
                return s
    
    
    def sort_dictionary(self, dic):
        return sorted(dic.items(), key=lambda item: item[1])


    def print_population(self):
        for s in self.pop:
            print(f'{s.get_id()}, {s.get_distance()} {s.get_fitness()}')

    def new_solution(self, client_list):
        try:
            aux = self.pop[0]
            new_s = Solution(None, aux.get_adj_matrix(), aux.get_capacity(), self.last_id)
            new_s.set_client_list(client_list)
            new_s.initial_solution()
            return new_s
        except :
            print('offspring error')



    
    
if __name__ == '__main__':

    p = Population(3)
    p.new_population('c0530.txt')
    p.print_population()
    p.reverse_sorted()


  

