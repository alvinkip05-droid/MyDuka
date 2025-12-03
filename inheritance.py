class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return "General sound"
    
class Dog(Animal):
    def speak(self):
        return "Barks"
    