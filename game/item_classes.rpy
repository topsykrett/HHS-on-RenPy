init -50 python:
    class Item:
        def __init__ (self, name, cost, image):
            self.name = name
            self.cost = cost
            self.image = image
    
    class Tool(Item):
        def __init__ (self, count):
            self.count = count
    
    class Clothing(Item):
        def __init__ (self, cover, lust, corr, reputation):
            self.cover = cover
            self.lust = lust
            self.reputation = reputation
    
    class Toy(Item):
        def __init__ (self, cover, size, corr, lust):
            self.cover = cover
            self.soze = size
            self.corr = corr
            self.lust = lust