class Client:

    def __init__(self, id, delivery, pickup):
        self.id = id
        self.pickup = pickup
        self.delivery = delivery
        self.x = None
        self.y = None
    
    def __init__(self, x, y , id, delivery, pickup) :
        self.x = x
        self.y = y
        self.id = id
        self.pickup = pickup
        self.delivery = delivery
    
    def __repr__(self):
        return '{}'.format(self.id)
    
    # def __repr__(self):
    #     return '{}'.format(self.id)
    
    def get_id(self):
        return self.id
    
    def get_pickup(self):
        return self.pickup
    
    def get_delivery(self):
        return self.delivery
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def print_client(self):
        return 'Client id {}, pickup {}, delivery {}'.format(self.id, self.pickup, self.delivery)
    