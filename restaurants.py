# restaurants.py 

class Restaurant:
    def __init__(self, name):
        self.name = name  
        
    def name(self):
        return self.name
        
restaurant1 = Restaurant("The Cafe Java")
print(restaurant1.name)