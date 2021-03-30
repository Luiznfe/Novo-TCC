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
    
    def teste(self, pop_size, s):
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        g.fitness_function(p)
        # p.print_population()
        p_cross = 0.3
        for i in p.get_population():
            if random.random() <= 0.3:
                g.crossover(i, p, p_cross)
        print('-'*20)
        p.print_offsprings()
        print('-'*20, 'mutation')
        p_mut = 0.1
        for i in p.get_offsprings():
            if random.random() <= p_mut:
                g.mutation(i, p_cross, p_mut)
        # p.print_offsprings()
        

    def run(self, pop_size, e_time):
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        # for i in p.get_population():
        #     funcs.local_search(i)
        while True:
            g.fitness_function(p)
            # p.print_population()
            parents = []
            parents = g.tournamet_selection(p, 3)
            g.crossover(parents, p)
            # for i in p.get_population():
            #     funcs.local_search(i)
            g.mutation(p)
            for i in p.get_population():
                funcs.local_search(i)
            g.survivior_selection(p)
            if e_time < 0:
                break
            e_time -= 1
        print('-'*20)
        p.print_population()
        # print('tempo ', fim - ini)

if __name__ == '__main__':
   
    m = Main(sys.argv[1], sys.argv[2])