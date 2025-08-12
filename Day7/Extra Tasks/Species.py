class Dog:
    species = "Canis familiaris" 

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

print(dog1.describe())  
print(dog2.describe())  

dog1.species = "Modified species"

print(dog1.describe()) 
print(dog2.describe())  


print(Dog.species)