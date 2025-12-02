class person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
        self.is_married= is_married
       
       
       
person1 = person("Alvin",21,174,"kimathi st",False)
print(person1) 
print(type(person1))
print(person1.name)        





class Person:
    def __init__(self, name, age, height, address, is_married):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
        self.is_married = is_married

    def greet(self):
        return f"Hi my name is {self.name}"

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, height={self.height}, address={self.address}, married={self.is_married})"


person1 = Person("Alice",25,"170cm","Kimathi St",False)
person2 = Person("Alvin",20,"178cm","Kimathi St",False)

print(person1)          
print(type(person1))     
print(person1.name) 
print(person1.address)
print(person1.greet())
