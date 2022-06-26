class bikeshop():
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total bikes avaliable :",self.stock)
    def rentabike(self,q):

        if q <= 0 :
            print("Enter the positive value or greater than zero :")
        elif q > self.stock:
            print("Enter the value less than stock :")
        else:
            self.stock=self.stock-q
            print("Total prices :",q *100)
            print("Total bikes avaliable :",self.stock)

while True:
    obj = bikeshop(100)
    uc = int(input('''
    1 Display stocks
    2 Rent a bike
    3 Exit
        ''' ))            

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the quantity : "))
        obj.rentabike(n)
    else:
        break         