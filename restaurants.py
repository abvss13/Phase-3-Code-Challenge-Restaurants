# restaurants.py 

class Restaurant:
    def __init__(self, name):
        self.name = name  
        
    def name(self):
        return self.name
        
restaurant1 = Restaurant("The Plaza Hotel")
print(restaurant1.name)