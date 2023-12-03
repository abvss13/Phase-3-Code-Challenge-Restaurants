# app.py

from customers import Customer
from restaurants import Restaurant

customer1 = Customer("Harry", "Maguire") 
restaurant1 = Restaurant("The Plaza")

print(customer1.full_name())
print(restaurant1.name)