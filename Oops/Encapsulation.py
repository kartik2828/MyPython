# How to use getter and setter method in Python

class student:
    def __init__(self):
        self.__name = ""

    def getname(self):    #Getter method (basically used to get the value)
        return self.__name

    def setname(self,name):  #Setter method  (basically used to set the values)
        self.__name=name

obj = student()
obj.setname("Kartik")
name = obj.getname()
print(name)

--------------------------------------------------------------------------------------------------
# Program 1

class student:
    __name = "Kartik"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()

    def __displayinfo(self):
        print("Hello Kartik")

obj = student()

