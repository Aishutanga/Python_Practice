if 24 > 18:
    print(" Your are above 18")
# Indentation required 

# Input and output 
# Use print() to display output.
# Use input() to take user input.
name = input("Enter your name: ")
print("I am "+ name)

#Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(" my age is "+ str(self.age))  
p = Person("Aishwarya", 24);
p.greet()       