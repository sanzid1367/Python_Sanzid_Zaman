class Dog:
    
    def __init__(self, name="Unnamed", breed="Mixed"):
        
        self.__name = name
        self.__breed = breed

    def Bark(self):
        print(f"Dog {self.__name} barked: Woof! Woof!")

    def set_name(self, new_name):
        self.__name = new_name
 
    def get_name(self):
        return self.__name
        
    def get_breed(self):
        return self.__breed

dog1 = Dog()
dog1.set_name("Buddy")  
dog1.Bark()

dog2 = Dog("Max", "German Shepherd")
dog2.Bark()

print("Second Dog Name:", dog2.get_name())
print("Second Dog Breed:", dog2.get_breed())