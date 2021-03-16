
# Create a parent class
class Furniture:
    room = ""
    weight = 0
    price = 0
    
    def  __init__(self, room, weight, price):
        self.room = room
        self.weight = weight
        self.price = price
    
    def upgrade(self, newprice):
        increase = newprice - self.price
        self.price = newprice
        return increase

# Create a child class
class Bed(Furniture):
    room = "Bedroom"
    size = ""
    bedType = ""

    def __init__(self, size, bedType):
        self.room = "Bedroom"
        self.size = size
        self.bedType = bedType

    # Changing parent class method (polymorphism!)
    def upgrade(self, frameStyle, framePrice, newPrice):
        """ For adding a frame or upgrading bed """
        self.price = self.price + framePrice
        self.frameStyle = frameStyle
        self.price = newPrice
        return framePrice

# Create a second child class    
class Couch(Furniture):
    room = "Living Room"
    couchType = ""
    color = ""

    def __init__(self, couchType, color):
        self.room = "Living Room"
        self.couchType = couchType
        self.color = color    

    # Changing parent class method (polymorphism!)
    def upgrade(self, newColor, newPrice):
        """ For reupholstering or upgrading couch """
        self.color = "newColor"
        increase = newPrice - self.price
        self.price = newPrice
        return increase


if __name__ == "__main__":
    # Testing Furniture Class
    totalUpgrades = 0
    table01 = Furniture("", 20, 400)
    print("Table price: $" + str(table01.price))

    # Testing child Classes
    bed01 = Bed("King", "Standard")
    couch01 = Couch("Sleeper Sofa", "Green")

    # Testing child Class methods
    totalUpgrades = totalUpgrades + bed01.upgrade("Plain metal", 200, 800)
    totalUpgrades = totalUpgrades + couch01.upgrade("Red", 500)
    print("Total Upgrades: $" + str(totalUpgrades))

