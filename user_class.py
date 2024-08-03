
# Parent class
class User:
    def __init__(self, name, city, state, zip_code, address):
        self.name = name
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.address = address

# Call the search() method for user1 object
    def search(self):
        print(f"Hello, my name is {self.name}. I need an arborist to remove some trees for me. I am from {self.city} {self.state}. My street address is {self.address}")

# Object created for parent (User) class with the following attributes
user1 = User("Corey", "Alamosa", "CO", 81101, "705 Diamond dr")

# search() method for the user1 object of the parent class
user1.search()

# Sub class (Arborist) of parent class (User)
class Arborist(User):
    def __init__(self, business_name, service_type, price, years_experience, reviews):
        self.business_name = business_name
        self.service_type = service_type
        self.price = price
        self.years_experience = years_experience
        self.reviews = reviews
    
    # Call the search() method for the arborist1 object

    # Override search() method
    def search(self):

        # call the search() method of parent class using super() function
        super().search()
        
        print(f"Hello Corey, this is {self.business_name} and I would love to help you with your tree problems")
    
    # Object created for sub class (Arborist) with the following attributes
arborist1 = Arborist("Treezbgone", "tree removal", 1000, 5, "five stars")

arborist1.search