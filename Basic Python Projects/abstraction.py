"""
Creating a class that utilizes the concept of abstraction.
1. Contains an abstract method and one regular method.
2. Includes a child class that defines the implementation of its parent's abstract method.
3. Creates an object that utilizes both the parent and child methods.
"""

from abc import ABC, abstractmethod

# Parent class, with a regular method and abstract method.  It seems you can't instantiate a class with an abstract method.
class credit(ABC):
# A regular method within the abstract class. Can use normally.
    def limit(self, total):
        print("Total credit remaining: {}".format(total))

# Creating abstract method to be defined by subclasses
    @abstractmethod
    def newCard(self, cardNo):
        pass

# Subclass implementing abstract class.
class lostCard(credit):
    def newCard(self, cardNo):
        print("Your card will be mailed soon. Please check to confirm this is for the card ending in {}.".format(cardNo[-4:]))


if __name__ == "__main__":
    myRequest = lostCard()
    myRequest.limit(2000)
    
    myRequest.newCard("1234 5678 9101 1112")
    
        
