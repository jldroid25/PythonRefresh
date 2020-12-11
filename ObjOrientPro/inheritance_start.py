#----------Inheritance in Python ---------------#

class stadiagames:
    
    # Let's override the init function
    '''
    __init__() is a special Python function . __init__() is called when
    the instance is created and ready to be initialized
    '''
    def __init__(self, title, company, developer, price):
        # TODO: add properties (AKA instance attribute)
        self.title = title
        self.company = company
        self.developer = developer
        self.price = price

    # now lets add an instance methods
    #  for the  price
    def getprice(self):
        return self.price

# Create instance of book class
firstgame = stadiagames("Death by Daylight", "Ubisoft", "DAve Marino", "$59.99") 
secondgame= stadiagames("Lola 2 Brat","Euphoria-Soft", "N-Princess", "$250")

print("\n\n")
# Le's call the getprice() instance method
print(firstgame.getprice())


#print("Expensive Stadai Pro Games: ")
#print(firstgame.title)

print("\n")