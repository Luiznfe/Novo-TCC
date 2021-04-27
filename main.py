from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import random
import funcs 
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
        p.new_population('c0530.txt')
        return p
    
    def teste2(self, pop_size, s):
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        g.fitness_function2(p.get_population(), p)
    
    def teste(self, pop_size, s):
        # população iniciada
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        print('pop inicial')
        p.print_population()
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
            # off_seze rebe a quantidade de filhos gerados
            off_size = len(p.get_offsprings())
            # fitness dos filhos é calculado
            g.fitness_function(p.get_offsprings(), p)
            # print('-'*20, 'offsprings')
            # p.print_offsprings()
            # print('-'*20,)
            # definida a probabilidade de mutação
            # DECIDIR A PROB DE MUTAÇÃO
            p_mut = 0.2
            for i in p.get_offsprings():
                if random.random() <= p_mut:
                    g.mutation(i, p_cross, p_mut)
            g.fitness_function(p.get_offsprings(), p)
            # print('-'*20,'ops muta')
            g.survivior_selection(p, pop_size)
            # p.print_offsprings()
            s -= 1
            if s == 0:
                break
        print('new pop')
        p.print_population()
        

if __name__ == '__main__':
   
    m = Main(sys.argv[1], sys.argv[2])