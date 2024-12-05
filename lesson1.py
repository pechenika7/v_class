class Dress:
    color = None
    price = 0
    def __init__(self, c= None):
        if c != None:
            self.color = c

    def SetPrice(self, p):
        self.price = p

    def SetColor(self, p):
        self.color = p

a = Dress('purple')
b = Dress('black')
c = Dress()
print(a.color, b.color, c.color, a.price, b.price, c.price)
Dress.color = 'yellow'
d = Dress()
a.SetPrice(500)
Dress.price = 300
print(a.color, b.color, c.color, d.color, a.price, b.price, c.price)
c.SetColor('magenta')
print(a.color, b.color, c.color, d.color, a.price, b.price, c.price)