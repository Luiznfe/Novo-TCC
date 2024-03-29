class Vehicle:

    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.route = list()
        self.distance = 0
        self.load = 0
    
    def __repr__(self):
        return '{}, {}'.format(self.id, self.distance)
    
    def get_id(self):
        return self.id
    
    def get_capacity(self):
        return self.capacity

    def get_route(self):
        return self.route
    
    def get_distance(self):
        return self.distance

    def set_distance(self, dis):
        self.distance = dis
    
    def set_route(self, r):
        self.route.clear()
        self.route = r[:]
    

    # Acho que n preciso da cópia
    def check_route(self):
        # cria uma copia da rota
        copy_route = self.route[:]
        # load recebe a carga a ser entregue na rota
        # load recebe a carga total da rota e uma verificação é feita cliente por cliente
        # para ver se nenhum ponto visitado excede a capacidade do veículo
        load = 0
        for c in copy_route:
            try:
                load += float(c.get_delivery())
            except :
                print(copy_route)
        if load > self.capacity:
            return 0
        for i in copy_route:
            load -= float(i.get_delivery())
            load += float(i.get_pickup())
            if load > self.capacity:
                return 0
        return 1
          
        
    def add_client(self, client):
        # adiciona o cliente na rota
        self.route.append(client)
        # verifica se a rota ainda pode ser aceita
        # caso não o cliente é retirado e a func retorna 0
        f = self.check_route()
        if f == 0:
            self.route.pop()
            return 0
        return 1

    def sum_distance(self, dist):
        self.distance += float(dist)
    
    
    def sequence(self):
        seq = []
        for i in self.route:
            seq.append(i.get_id())
        return seq
    
    # retorna ids de uma rota (sem o deposito)
    def route_ids(self):
        r_ids = list()
        for i in self.route:
            if i.get_id() != 0:
                r_ids.append(i.get_id())
        return r_ids        
    
    def print_route(self):
        aux = list()
        for i in self.route:
            aux.append(i.get_id())
        print(aux)
    
    def get_corr(self):
        x = list()
        y = list()
        for i in self.route:
            x.append(i.get_x())
            y.append(i.get_y())
        return x, y
    
    def print_vehicle(self):
        return 'vehicle id {}, capcity {}, distatance {}'.format(self.id, self.capacity, self.distance)