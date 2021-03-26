from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import funcs 
from read import Read
import time

p = Population(20)
p.new_population('c0530.txt')
g = GeneticAlgorithm()
p.print_population()
ini = time.time()
while True:
    g.fitness_function(p)
    parents = []
    parents = g.tournamet_selection(p, 3)
    g.crossover(parents, p)
    g.mutation(p)
    g.survivior_selection(p)
    fim = time.time()
    if fim - ini > 60:
        break

print('-'*20)
p.print_population()
print('tempo ', fim - ini)