class Car:
    brand = None
    color = None
    price = 0
    cabin = None

    def __init__(self, b, c, cab):
        self.brand = b
        self.color = c
        self.cabin = cab

    def SetPrice(self, p):
        self.price = p

car1 = Car('Toyota', 'white', 'sedan')
car1.SetPrice(5000)
car2 = Car('BMW', 'black', 'sedan')
print(car1.price, car2.price)