class phone:

    def __init__(self,brand,price):  # for constructors
        self.brand=brand
        self.price=price


    def call(self,phoneNumber): # self is like this in java
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self) ->str: # the methode return a string data type
        return f"Brand = {self.brand} \n Price = {self.price}"


iphone = phone("iphone 7+",100)  #  "iphone 7+",100 is the actual init
samsung = phone("samsung",100)

print(iphone.brand)
print(iphone.price) #properties
iphone.call(2344) # behaviour

print("Phones ")
print(iphone)
print(samsung)
"""
print the object is not yet possible 
"""
