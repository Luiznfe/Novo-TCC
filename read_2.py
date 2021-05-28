from scipy.spatial import distance
from client import Client

class Read2:
    
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
    
    def new_matrix(self):
        adj_matrix = list()
        aux = list()
        
        data = self.open_file()
        n, cap = data.pop(0).strip().split()
        data.insert(0, '0 0 0 0 ')
    
        for i in range(len(data)):
            a = tuple(map(int, data[i].split()[:2]))
            for j in range(len(data)):
                b = tuple(map(int, data[j].split()[:2]))
                dst = distance.euclidean(a, b)
                aux.append(round(dst, 4))
            adj_matrix.append(aux[:])
            aux.clear()
        return adj_matrix, n , cap, data
                
    def create_instance_2(self):
        adj_matrix, n , cap, data = self.new_matrix()
        client_list = list()
        data.pop(0)
        id = 0
        for i in data:
            a = tuple(map(int, i.split()))
            c = Client(a[0], a[1], id, a[2], a[3])
            id += 1
            client_list.append(c)
        return float(cap), client_list, adj_matrix
    
            
            

        
    
    
if __name__ == '__main__':
    
    r = Read2('c2.txt')
    r.client_list()