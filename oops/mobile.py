#create or constructor=>initializing instance variable
#java c++=>constructor is similar to class name
#js=>constructor name is constructor()
#python=>__init__
class mobile:
    model:str
    color:str
    brand:str
    price:int

    def __init__(self,model,color,brand,price):
        self.model=model
        self.color=color
        self.brand=brand
        self.price=price
    def display_details(self):
        print(self.model,self.brand,self.price)
obj1=mobile("a52","blue","oppo",18000)
obj1.display_details()