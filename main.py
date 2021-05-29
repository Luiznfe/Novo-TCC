from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import random
import funcs 
import funcs2 
from read import Read
import time
import sys

class Main:

    def __init__(self, size, time):
        self.size = int(size)
        self.time = int(time)
        self.teste(self.size, self.time)

    def create_pop(self, size):
        p = Population(size)
        p.new_population_2('c2.txt')
        return p
    
    def teste2(self, pop_size, s):
        n_ls = 200
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        
        for i in p.get_population():
            funcs2.local_search(i, 100)
            
        g.fitness_function(p.get_population(), p)
        
        p_cross = 0.3  # 30%
        f = 0
        for i in p.get_population():
            if random.random() <= 0.3:
                g.crossover(i, p, p_cross)
            
                
        for j in p.get_population():
            funcs2.local_search(j, n_ls)
            
        for f in p.get_offsprings():
            funcs2.local_search(f, n_ls)
        
        a = p.get_offsprings()[0]
        
        p_mut = 0.3
        for i in p.get_offsprings():
            if random.random() <= p_mut:
                g.mutation(i, p_mut)
        
        for i in p.get_population():
            if random.random() <= p_mut:
                g.mutation(i, p_mut)
        
        g.survivior_selection(p, pop_size)
                
        
        # # LOCAL SEARCH
        # start = time.time()
        # for j in p.get_population():
        #     funcs2.local_search(j, n_ls)
        # while True:
        #     g.fitness_function(p.get_population(), p)
        
        #     p_cross = 0.3  # 30%
        #     f = 0
        #     for i in p.get_population():
        #         if random.random() <= 0.3:
        #             g.crossover(i, p, p_cross)

        #     for j in p.get_population():
        #         funcs2.local_search(j, n_ls)
            
            
        #     for f in p.get_offsprings():
        #         funcs2.local_search(f, n_ls)
        
        #     off_size = len(p.get_offsprings())
        #     # fitness dos filhos é calculado
        #     g.fitness_function(p.get_offsprings(), p)

        #     p_mut = 0.3
        #     for i in p.get_offsprings():
        #         if random.random() <= p_mut:
        #             g.mutation(i, p_mut)
                
        #     for f in p.get_offsprings():
        #         funcs2.local_search(f, n_ls)
        
        #     g.fitness_function(p.get_offsprings(), p)
        
        #     g.survivior_selection(p, pop_size)
        #     s -= 1 
        #     if s == 0:
        #         break
        
        # stop = time.time()
        # print(stop - start)
        # # while True:
            
        # #     s -= 1
        # #     if s == 0:
        # #         break
    
    def teste(self, pop_size, s):
        # n de iterações da busca
        n_ls = 100
        # população iniciada
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        # LOCAL SEARCH
        for j in p.get_population():
            funcs2.local_search(j, n_ls)
        #p.best_solution()
        while True:
            # fitness calculado
            g.fitness_function(p.get_population(), p)
            # print('pop inicial')
            # p.print_population()
        # definida a probabilidade de crossover
            p_cross = 0.3  # 30%
            for i in p.get_population():
                if random.random() <= 0.3:
                    g.crossover(i, p, p_cross)
            # LOCAL SEARCH
            for j in p.get_population():
                funcs2.local_search(j, 30)
            # busca local nos filhos
            for f in p.get_offsprings():
                funcs2.local_search(f, 30)
            # off_seze rebe a quantidade de filhos gerados
            off_size = len(p.get_offsprings())
            # fitness dos filhos é calculado
            g.fitness_function(p.get_offsprings(), p)
            # definida a probabilidade de mutação
            # DECIDIR A PROB DE MUTAÇÃO
            p_mut = 0.3
            for i in p.get_offsprings():
                if random.random() <= p_mut:
                    g.mutation(i, 0.3)
            # busca local nos filhos
            for f in p.get_offsprings():
                funcs2.local_search(f, 30)
            g.fitness_function(p.get_offsprings(), p)
            # print('-'*20,'ops muta')
            g.survivior_selection(p, pop_size)
            # p.print_offsprings()
            s -= 1
            if s == 0:
                break
        print('new pop')
        p.best_solution()
        

if __name__ == '__main__':
   
    m = Main(sys.argv[1], sys.argv[2])