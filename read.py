from client import Client

class Read:

    def __init__(self, path):
        self.path = path

    def open_file(self):
        data = list()
        try:
            file = open(self.path)
            data = file.readlines()
            return data
        except:
            print('Something went wrong with the file')
    
    def create_instance(self):
        data = self.open_file()
        # cap recebe a capacidade da frota
        cap = float(data[0])
        data.pop(0)
        # qt_clients recebe a quantidade de clientes
        qt_clients = int(data[0])
        data.pop(0)
        # criando a matriz de adjacencia 
        adjMatrix = list()
        self.adj_matrix(qt_clients, data, adjMatrix)
        # criando uma lista de clientes
        c_list = list()
        self.create_client_list(data, c_list)
        return cap, c_list, adjMatrix
    
        
    def create_client_list(self, data, c_list):
        # percorre a lista data e inicia um objeto cliente para cada par 
        # delivery/pickup
        id = 1
        for i in range(0, len(data) , 2):
            c = Client(id, data[i], data[i + 1])
            c_list.append(c)
            id += 1   

    def adj_matrix(self, b, data, adj):
        # percorre a lista e adiciona os dados a uma lista line
        # adiciona os da lista line na matriz
        line = list()
        for i in range(0, b + 1):
            for j in range(0, b + 1):
                line.append(data[j])
            adj.append(line[:])
            line.clear()
            for j in range(0, b + 1):
                data.pop(0)

        

if __name__ == '__main__':

    r = Read('C:/Users/luizn/Desktop/TCC/c0530.txt')
    r.open_file()
            
