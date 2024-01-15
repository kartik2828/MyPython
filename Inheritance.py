# Single inheritance 

class A:
    def displayA(self):
        print("Welcome to New world A")

class B(A):
    def displayB(self):
        print("Welcome to New World B")

obj = B()
obj.displayA()
obj.displayB()


# Multilevel Inheritance 

class A:
    def displayA(self):
        print("Welcome to New world A")

class B(A):
    def displayB(self):
        print("Welcome to New World B")

class C(B):
    def displayC(self):
        print("Welcome to New World C")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()


# Multiple Inheritance 

class A:
    def displayA(self):
        print("Welcome to New world A")

class B:
    def displayB(self):
        print("Welcome to the New world B")

class C(A,B):
    def displayC(self):
        print("Hello world")

obj = C()
obj.displayC()
obj.displayB()
obj.displayA()

# Java and PHP does not support multiple inheritance





