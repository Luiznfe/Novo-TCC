from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
from read import Read

p = Population(11)
p.new_population('c0530.txt')

g = GeneticAlgorithm()
g.fitness_function(p)
# p.print_population()
print('Parents','-'*20)
parents = []
parents = g.tournamet_selection(p, 3)
g.crossover(parents, p)
# print(parent)

