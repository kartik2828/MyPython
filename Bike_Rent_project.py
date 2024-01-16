class bike:
    def __init__(self,stock):
        self.stock = stock
    def display_bike(self):
        print("Total Bikes",self.stock)

    def rentForBikes(self,quantity):

        if quantity<=0:
            print("Enter a positive value")
        elif quantity>self.stock:
            print("Enter the value Less than stock")

        else:
            print("Total price", quantity*100)
            print("Total bikes left",(self.stock - n))

while True:
    obj = bike(100)
    uc = int(input(
        '''
        1. Display Stocks
        2. Rent a bike
        3. Exit
        '''
    ))
    if uc==1:
        obj.display_bike()
    elif uc==2:
        n = int(input("Enter a quantity: "))
        obj.rentForBikes(n)
    else:
        break
