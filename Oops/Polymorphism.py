# polymorphism (function name is same but different in features)

# Example - In this example, I am using the len() function but doesn't matter which datatype I am taking, It will work the same for all.

l1 = [1,2,3,4,5]
print(len(l1))

str1 = "Kartik"
print(len(str1))

------------------------------------------------------------------------------------------------------------------
# Method Overloading

class my_class:
    def displayinfo(self, name=""):
        print("Hello Kartik" + name)

obj = my_class()
obj.displayinfo()
obj.displayinfo(" Sharma")   # Here we have the same function name but diff in parameters which is called method overloading


# Diff bw Method overloading & method overriding
# Overloading always be in the same class but overriding be in a different class with the same function name
-------------------------------------------------------------------------------------------------------------------

# Method Overloading
class area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print("Area of rectengle is: ",(x*y))

        elif x!=None:
            print("Area of square is ",(x*x))

        else:
            print("Nothing")

obj = area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

-----------------------------------------------------------------------------------------------------------------------

# Method Overriding

class A:
    def _displayinfo(self):
        print("Hello Kartik")

class B(A):
    def _displayinfo(self):
        print("Hello Sharma ji")
        super()._displayinfo()  # We use a super keyword to call the parent class function

obj = B()
obj._displayinfo()  # It will always print // Hello sharma ji, bcoz child class function will override the parent class function







