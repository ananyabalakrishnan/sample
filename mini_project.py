class Dog:
    species = "Canis familiaris" #class attribute
    #instance attributes:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #method
    def bark(self):
        return "Woof!"
#instances:
dog1 = Dog("Lily", "Part Chihuahua part scary")
dog2 = Dog("Chiku", "Golden Retriever")

print(dog1.name)
print(dog2.breed)
print(Dog.species)

print(dog1.bark()) #output: Woof!