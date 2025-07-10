class Product:
    def __init__(self, id=-1, name="", price=-1.0):
        self.Name = name
        self.Id = id
        self.Price = price
    def __repr__(self):
        return f"({self.Id}, {self.Name}, {self.Price})"    