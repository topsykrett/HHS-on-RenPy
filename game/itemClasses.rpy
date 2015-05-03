init -50 python:
    class Item:
        def __init__ (self, name, cost, durability, picto):
            self.durability = durability
            self.name = name
            self.cost = cost
            self.picto = picto
            self.type = type
            
    class Tool(Item):
        def __init__ (self, purpose):
            self.purpose = purpose
            
    class Clothing(Item):
        def __init__ (self, lust, corr, reputation, char, sex, purpose):
            self.cover = []
            self.lust = lust
            self.corr = corr
            self.reputation = reputation
            self.char = char
            self.sex = sex
            self.purpose = purpose
    
    class Toy(Item):
        def __init__ (self, cover, size, corr, lust):
            self.cover = cover
            self.soze = size
            self.corr = corr
            self.lust = lust          

    class Food(Item):
        def __init__ (self, energy):
            self.energy = energy