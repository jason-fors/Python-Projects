

# Creating class "Engine" with protected and private variables.

class Engine:
    def __init__(self):
        # Setting a protected attribute. Just a naming convention. Doesn't actually change anything.
        self._fuelinjection = True

    # This gets the protected attribute, but isn't necessary.
    def getFI(self):
        print(self._fuelinjection)

    def compression(self):
        # Setting a private attribute
        self.__compressionratio = 12  # This variable name gets mangled by Python.

    def getCompression(self):
        # Method to get the value of the private variable. Necessary to access from outside the class.
        print(self.__compressionratio)
        return self.__compressionratio
        
    def setCompression(self, newRatio):
        # Method to set the value of the private variable. Necessary to change from outside the class.
        self.__compressionratio = newRatio





if __name__ == "__main__":
    myEngine = Engine()
    myEngine.compression()

    print(myEngine._fuelinjection)
    myEngine._fuelinjection = False
    myEngine.getFI()
    
    #print(myEngine.__compressionratio)  Won't work. Name not recognized.
    myEngine.__compressionratio = 5  # This creates a new object variable, distinct from private variable.
    
    myEngine.getCompression()
    myEngine.setCompression(13)
    myEngine.getCompression()

    watchthis = myEngine.getCompression() + myEngine.__compressionratio
    print("Adding created object variable value to the private one in the class method obtained using in-class method: " + str(watchthis))
    
    

