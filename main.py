from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import local_search
import funcs 
from read import Read
import time
import sys

class Main:

    def __init__(self, size, time):
        self.size = int(size)
        self.time = int(time)
        self.run(self.size, self.time)

    def create_pop(self, size):
        p = Population(size)
        p.new_population('c0530.txt')
        p.print_population()
        return p
    
    def teste(self, pop_size, s):
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        for i in p.get_population():
            funcs.local_search(i)
        print('-'*20)
        p.print_population()
        

    def run(self, pop_size, e_time):
        g = GeneticAlgorithm()
        p = self.create_pop(pop_size)
        for i in p.get_population():
            funcs.local_search(i)
        while True:
            g.fitness_function(p)
            parents = []
            parents = g.tournamet_selection(p, 3)
            g.crossover(parents, p)
            for i in p.get_population():
                funcs.local_search(i)
            g.mutation(p)
            # for i in p.get_population():
            #     funcs.local_search(i)
            g.survivior_selection(p)
            if e_time < 0:
                break
            e_time -= 1
        print('-'*20)
        p.print_population()
        # print('tempo ', fim - ini)

if __name__ == '__main__':
   
    m = Main(sys.argv[1], sys.argv[2])
    # p = Population(size)
    # p.new_population('c0530.txt')
    # p.print_population()
    # g = GeneticAlgorithm()
    # g.survivior_selection(p)

# p = Population(20)
# p.new_population('c0530.txt')
# g = GeneticAlgorithm()
# p.print_population()
# ini = time.time()
# while True:
#     g.fitness_function(p)
#     parents = []
#     parents = g.tournamet_selection(p, 3)
#     g.crossover(parents, p)
#     g.mutation(p)
#     g.survivior_selection(p)
#     fim = time.time()
#     if fim - ini > 60:
#         break

# print('-'*20)
# p.print_population()
# print('tempo ', fim - ini)