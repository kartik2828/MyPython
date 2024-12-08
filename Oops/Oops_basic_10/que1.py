# Question 1:
# Define a class `Person` with attributes `name` and `age`.
# Add a method `greet` that prints "Hello, my name is {name} and I am {age} years old."

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hello, my name is {self.name} and I am {self.age} years old.')

obj = person('Kartik',23)
obj.greet()


