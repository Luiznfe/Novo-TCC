import matplotlib.pyplot as plt
class Plot:
    
    def __init__(self, solution):
        self.solution = solution
    
    def plot(self):
        vehicles = self.solution.get_vehicle_list()
        x_corr = list()
        y_corr = list()
        id = 1
        for v in range(len(vehicles)):
            x_corr, y_corr = vehicles[v].get_corr()
            self.run(x_corr, y_corr, id)
            if v == 3:
                break
        
        self.show()
    
    def run(self, x, y, id):
        plt.plot(x, y, label = "route" )
    
                        
    def show(self):
        plt.show()
    