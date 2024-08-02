
class User:

    home_type = 'woodland'
    def __init__(self, name, location, price, service, address):
        self.name = name
        self.location = location
        self.price = price
        self.service = service
        self.address = address

corey = User('name', 'location', 'price', 'service', 'address')
corey.name = "Corey" 
corey.location = "Alamosa CO 81101" 
corey.price = 1000 
corey.service = "storm damage repair"
corey.address = "705 Diamond dr"

don = User('name', 'location', 'price', 'service', 'address')
don.name = "Don" 
don.location = "CO Springs, CO 56272" 
don.price = 600
don.service = "stump pruning"  
don.address = "123 Murphy str"

def search_arborist(self):
    print (f"My name is {self.name} I live in {self.location} I'm looking for an arborist and I need {self.servie} My price estimate is {self.price} and my street address {self.address}")

def search_arborist(self):
    print (f"My name is {self.name} I live in {self.location} I'm looking for an arborist and I need {self.servie} My price estimate is {self.price} and my street address {self.address}")          

    corey.search_arborist()
    don.search_arborist()
    