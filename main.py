from client import Client
from vehicle import Vehicle
from solution import Solution
from genetic_algorithm import GeneticAlgorithm
from population import Population
import funcs 
from read import Read

p = Population(30)
p.new_population('c0530.txt')

g = GeneticAlgorithm()
g.fitness_function(p)
print('Inicial Pop','-'*20)
p.print_population()
print('-'*20)
parents = []
parents = g.tournamet_selection(p, 3)
g.crossover(parents, p)
print('Cross','-'*20)
p.print_population()
print('-'*20)
g.mutation(p)
g.survivior_selection(p)
print('Pop','-'*20)
p.print_population()
print('-'*20)
