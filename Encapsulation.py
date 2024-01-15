# How to use getter and setter meathod in Python

class student:
    def __init__(self):
        self.__name = ""

    def getname(self):    #Getter meathod (basically used to get the value)
        return self.__name

    def setname(self,name):  #Setter meathod  (basically used to set the values)
        self.__name=name

obj = student()
obj.setname("Kartik")
name = obj.getname()
print(name)

