
# Creating class user, with structure only.
class User:
    name = 'No Name Provided'
    email = ''
    accountNum = 0

    # Initialization method for class User taking 3 arguments.
    def __init__(self, name, email, accountNum):
        self.name = name
        self.email = email
        self.accountNum = accountNum

# Creating class Customer, a child class of User. Inherits attributes of User.
class Customer(User):
    address = ' '
    mailing_list = True

    # Initialization method for class Customer taking 3 arguments, including User object.
    def __init__(self, User, address, mailing_list):
        self.User = User
        self.address = address
        self.mailing_list = mailing_list

# Creating class Employee, a child class of User. Inherits attributes of User.
class Employee(User):
    employeeID = 0
    title = 'No title'

    # Initialization method for class Employee taking 3 arguments, including User object.
    def __init__(self, User, employeeID, title):
        self.employeeID = employeeID
        self.title = title

# Initiating classes, and printing values from initiated child classes.
if __name__ == "__main__":
    robertU = User("Robert", "bob@aol.org", 1)
    robertC = Customer(robertU, "1 Hill St", True)  # Passing in User object as argument
    susanU = User("Susan", "sue@books.com", 2)
    susanE = Employee(susanU, 25, "COO") # Passing in User object as argument

    print(robertU.name + " address: " + robertC.address)
    print(susanU.name + " title: " + susanE.title)




