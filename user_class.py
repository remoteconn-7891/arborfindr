# Base class
class User:

# Instances of base class
    home_type = 'woodland'
    def __init__(self, name, address, city, state, zip_code, price):
        self.name = name
        self.address = address
        self.city =city
        self.state = state
        self.zip_code = zip_code
        self.price = price

# Attributes of instances
corey = User('name', 'address', 'city', 'state', 'zip_code', 'address', 'price')
corey.name = "Corey" 
corey.address = "705 diamond dr" 
corey.city = "Alamosa"
corey.state = "CO"
corey.zip_code = 81101
corey.price = 1000

# Attributes of instances
don = User('name', 'address', 'city', 'state', 'zip_code', 'address', 'price')
don.name = "Don" 
don.address = "123 Murphy str" 
don.city = "CO Springs"
don.state = "CO"
don.zip_code = 57388
don.price = 1200

# Methods of objects
def search_arborist(self):
    print (f"My name is {self.name} I live in {self.city} {self.state} I'm looking for an arborist My price estimate is {self.price} and my street address {self.address}")

def search_arborist(self):
    print (f"My name is {self.name} I live in {self.city} {self.state} I'm looking for an arborist My price estimate is {self.price} and my street address {self.address}")          

    corey.search_arborist()
    don.search_arborist()
    
# Child class
class Arborist(User):
# Child class instances
    def __init__(self, business_name, service_type, price, reviews, years_of_experience):
        self.business_name = business_name
        self.service_type = service_type
        self.reviews = reviews
        self.years_of_experience = years_of_experience

# Attributes of instances
treetrimmerz = Arborist('business_name', 'service_type', 'reviews', 'years_of_experience')
treetrimmerz.business_name = 'Treetrimmerz'
treetrimmerz.service_type = 'consultation'
treetrimmerz.reviews = 'five stars'
treetrimmerz.years_of_experience = 10

def arborist_response(self):
    print (f"Hello this is {self.business_name} I would be happy to provide you with tree. I provide the following services {self.service_type} We can negotiate a price. 
           Please message me and we can work something out")

treetrimmerz.arborist_response()