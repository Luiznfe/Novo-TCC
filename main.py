from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import funcs 
from read import Read

p = Population(10)
p.new_population('c0530.txt')

g = GeneticAlgorithm()
g.fitness_function(p)
# p.print_population()
print('Parents','-'*20)
parents = []
parents = g.tournamet_selection(p, 3)
g.mutation(pop, 10)
# g.crossover(parents, p)
# print(parents[0])

# funcs.inversion(parents[0])
# print(parents[0])

