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
    
    def __repr__(self):
        return '{}, {}, {}'.format(self.id_solution, self.dist, self.fitness)
    
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
    def sum_dist(self, dist):
        self.dist += dist
    
    # embaralha a lista de clientes
    def random_client_list(self):
        a = self.client_list.pop(0)
        random.shuffle(self.client_list)
        self.client_list.insert(0, a)

    
    # set novo id
    def set_id(self, new_id):
        self.id_solution = new_id

    # set fitness
    def set_fitness(self, value):
        self.fitness = value
    
    def remove_depot(self):
        for i in range(len(self.client_list)):
            if self.client_list[i].get_id() == 0:
                a = i 
                break
        return self.client_list.pop(a)
        
    # gera uma solucao inicial
    def initial_solution(self):
        copy_client_list = list()
        copy_client_list = self.client_list[:]
        depot = copy_client_list.pop(0)
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
            self.sum_dist(v.get_distance())
            # incrementa 1 ao id do proximo veículo criado
            id += 1
            # print(f'distacia percorrida {v.get_distance()}')


    
    # retorna uma lista com apenas ids dos clientes sem o depósito
    def id_list(self):
        ids = list()
        for vehicle in self.get_vehicle_list():
            for client in vehicle.get_route():
                if client.get_id() != 0:
                    ids.append(client.get_id())
        return ids
    
    # retorna um cliente com base no id
    def get_client(self, id):
        for c in self.client_list:
            if c.get_id() == id:
                return c
        
    # retorna clientes com base em uma lista de ids passados
    def retrieve_list(self, c_list):
        # depot = Client(0, 0, 0)
        # self.client_list.append(depot)
        aux = list()
        for i in c_list:
            c = self.get_client(i)
            aux.append(c)
        return aux
    
    # adiciona o depoisto 
    def add_depot(self, r):
        r.insert(0, 0)
        r.append(0)
    
    # calcula a distancia de uma rota
    def check_distance_by_route(self, r):
        r_distance = 0
        for i in range(len(r) - 1):
            r_distance += float(self.adj_matrix[i][i + 1])
        return r_distance
    
    # calcula a distacia total das rotas 
    def check_new_distance(self, routes):
        new_distance = []
        # adiciona os depoisitos
        for i in routes:
            self.add_depot(i)
            new_distance.append(self.check_distance_by_route(i))
        # retorna 1 caso a nova distancia seja menor
        if sum(new_distance) < self.dist:
            return new_distance
        return 0
    
    # atualixa a solução com base nas novas rotas caso seja possível 
    def update_solution(self, routes):
        routes_copy = copy.deepcopy(routes)
        # verifica a nova distancia e retorna 0 caso seja maior que a antiga
        # ou uma lista com a distancia das rotas
        dis = self.check_new_distance(routes_copy)
        if dis == 0:
            return 0
        
        r_list = []
        # recupera os clientes com suas informações
        for i in routes_copy:
            r_list.append(self.retrieve_list(i))

        # cria um veículo para verificar se as rotas são possiveis
        # ATUALIZAR OS VEICULOS
        v_id = 0
        aux_v_list = []
        for i in r_list:
            v = Vehicle(v_id, self.cap)
            v.set_route(i)
            # verifica se a rota é possivel
            f = v.check_route()
            if f == 0:
                aux_v_list.clear()
                # retorna zero caso n seja possivel
                return 0
            # adiciona o veiculo
            aux_v_list.append(v)
            # incrementa o contador
            v_id += 1
            
        # atualiza a solução
        self.fitness = 0
        # atualizando a distancia das rotas
        for i in range(len(aux_v_list)):
            aux_v_list[i].set_distance(dis[i])
    
        # definindo uma novo lista de veiculos
        self.vehicle_list = aux_v_list[:]
        
        # atualizando a distancia da solução
        self.dist = sum(dis)
        return 1
    
    # Imprime as rotas
    def print_routes(self):
        for i in self.vehicle_list:
            i.print_route()
    
    
        
        
            
    

                


            
