class Beverage:
    def cost(self):
        return 0

    def description(self):
        return "beverage"

class Decorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost()

    def description(self):
        return self.beverage.description()

# The above is a fixed class, please do not modify it.
# Please complete other classes here >>
class Coffee(Beverage):
    def description(self):
        return "coffee"
    
    def cost(self):
        return 30

class BlackTea(Beverage):
    def description(self):
        return "blackTea"
    
    def cost(self):
        return 25

class GreenTea(Beverage):
    def description(self):
        return "greenTea"
    
    def cost(self):
        return 20

class Sugar(Decorator):
    def description(self):
        return self.beverage.description() + " + sugar"
    
    def cost(self):
        return self.beverage.cost() + 5

class Ice(Decorator):
    def description(self):
        return self.beverage.description() + " + ice"
    
    def cost(self):
        return self.beverage.cost() + 1

class Milk(Decorator):
    def description(self):
        return self.beverage.description() + " + milk"
    
    def cost(self):
        return self.beverage.cost() + 5

class Bubble(Decorator):
    def description(self):
        return self.beverage.description() + " + bubble"
    
    def cost(self):
        return self.beverage.cost() + 10

# << Please complete other classes here
# The following are the test cases, please do not modify them

beverages = [
    GreenTea(),
    Milk(Milk(BlackTea())),
    Milk(Ice(GreenTea())),
    Bubble(Milk(Ice(BlackTea())))
]

for b in beverages:
    if isinstance(b, Beverage):
        print(b.description(), "is a beverage!")
    else:
        print(b.description(), "is not a beverage?")
    print("Its price is", b.cost())

'''
Output:
greenTea is a beverage!
Its price is 20
blackTea + milk + milk is a beverage!
Its price is 35
greenTea + ice + milk is a beverage!
Its price is 26
blackTea + ice + milk + bubble is a beverage!
Its price is 41
'''
