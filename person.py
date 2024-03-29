class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Create a method called introduce inside the class
    def introduce(self):
       print(f"{self.name} is {self.age} years old, and he is a {self.gender}")

# Create an instance of the person class
person = Person("Emmanuel", 31, "Male")

person.introduce()