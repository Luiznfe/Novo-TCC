from client import Client
from vehicle import Vehicle
import random
import copy

class Solution:

    def __init__(self, client_list, adj_matrix, cap, id_solution):
        self.id_solution = id_solution
        self.vehicle_list = list()
        self.client_list = client_list
        self.adj_matrix = adj_matrix
        self.cap = cap  # capacidade de cada carro da frota
        self.dist = 0  # distancia percorrida pela frota
        self.fitness = 0 # fitness da solução
        self.age = 0
    
    def __repr__(self):
        return '{}, {}, {}, age {}'.format(self.id_solution, self.dist, self.fitness, self.age)

    def get_age(self):
        return self.age
    
    def plus_age(self):
        self.age += 1
    
    def get_id(self):
        return self.id_solution

    def get_vehicle_list(self):
        return self.vehicle_list[:]
    
    def get_clientList(self):
        return self.client_list[:]
    
    def get_adj_matrix(self):
        return self.adj_matrix
    
    def get_capacity(self):
        return self.cap
    
    def get_distance(self):
        return self.dist
    
    def get_fitness(self):
        return self.fitness
    
    def set_client_list(self, c_list):
        self.client_list = c_list[:]
    
    # limpa alguns componentes
    def reset_solution(self):
        self.vehicle_list.clear()
        self.dist = 0
        self.fitness = 0

    #  soma um valor a distancia total
    def total_distance(self, dist):
        self.dist += dist
    
    # embaralha a lista de clientes
    def random_client_list(self):
        random.shuffle(self.client_list)
    
    # set novo id
    def set_id(self, new_id):
        self.id_solution = new_id

    # set fitness
    def set_fitness(self, value):
        self.fitness = value
    
    # gera uma solucao inicial
    def initial_solution(self):
        # um deposito é criado
        depot = Client(0, 0, 0)
        copy_client_list = list()
        copy_client_list = self.client_list[:]
        id = 0 # id do veiculo
        while True: # enquanto existirem clientes ainda nao atendidos
            # para se a lista estiver vazia
            if len(copy_client_list) == 0:
                break
            # um novo carra é criado
            v = Vehicle(id, self.cap)
            # print(f'Veículo {id}')
            # index do primeiro cliente (doposito)
            index_client_1 = 0
            # deposito adicionado a lista
            v.add_client(depot)
            while True:
                # adiciona o ultimo cliente da lista ao veiculo
                client = copy_client_list[-1]
                f = v.add_client(client)
                if f == 0:
                    break
                # remove o cliente adicionado a rota da lista
                copy_client_list.pop()
                # recebe o index do cliente adicionado
                index_client_2 = client.get_id()
                # soma a distancia precorrida a distancia total do carro 
                current_distance = self.adj_matrix[index_client_1][index_client_2]
                v.sum_distance(current_distance)
                # print(f'cliente {index_client_1} para {index_client_2}, distancia {current_distance}')
                index_client_1 = index_client_2
                if len(copy_client_list) == 0:
                    break
            # soma a distancia entre o ultimo cliente da rota e o deposito
            last_distance = self.adj_matrix[index_client_2][depot.get_id()] 
            v.add_client(depot)
            v.sum_distance(last_distance)
            # print(f'cliente {index_client_2} para {depot.get_id()}, distancia {last_distance}')
            # adiciona o veiculo contendo a rota criada na lista da solução
            self.vehicle_list.append(v)
            # soma distancia da rota criada a distancia total da solução
            self.total_distance(v.get_distance())
            # incrementa 1 ao id do proximo veículo criado
            id += 1
            # print(f'distacia percorrida {v.get_distance()}')
    
    # # retorna um cliente com base no id
    # def get_client(self, id):
    #     clients = self.client_list
    #     for c in clients:
    #         if c.get_id() == id:
    #             return c
    
    # # retorna clientes com base em uma lista de ids passados
    # def get_new_client_list(self, c_list):
    #     aux = list()
    #     for i in c_list:
    #         aux.append(self.get_client(i))
    #     return aux
    
    # retorna uma lista com apenas ids dos clientes sem o depósito
    def get_sequence(self):
        seq = list()
        for vehicle in self.get_vehicle_list():
            for client in vehicle.get_route():
                if client.get_id() != 0:
                    seq.append(client.get_id())
        return seq
    
    # retorna um cliente com base no id
    def get_client(self, id):
        for c in self.get_clientList():
            if c.get_id() == id:
                return c
        
# retorna clientes com base em uma lista de ids passados
    def get_new_client_list(self, c_list):
        aux = list()
        for i in c_list:
            aux.append(self.get_client(i))
        return aux
        
    

                


            
