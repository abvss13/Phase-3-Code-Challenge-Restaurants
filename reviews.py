# reviews.py

class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer 
        self.restaurant = restaurant
        self.rating = rating
    
    def rating(self):
         return self.rating