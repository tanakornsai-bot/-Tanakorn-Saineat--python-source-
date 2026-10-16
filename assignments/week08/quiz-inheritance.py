""" 
Create a class hierarchy:

<<<<<<< HEAD
    Base class Vehicle with attributes: brand, model, model
=======
    Base class Vehicle with attributes: brand, model, year
>>>>>>> upstream/main
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
<<<<<<< HEAD
class Vehicle :
    def __init__(self, brand, model , year): #parameter แรก self เสมอ
        self.brand  =   brand
        self.model  =   model
        self.year   =   year

    def get_info(self):
        return f"Brand:{self.brand},Model:{self.model},Year:{self.year}"


class Car(Vehicle):

    def __init__(self,brand,model,year,number_of_door):
        super().__init__(brand,model,year)
        self.number_of_door = number_of_door

    def get_info(self):
        return f"Brand:{self.brand},Model:{self.model},Year:{self.year},Number of door:{self.number_of_door}"
    
=======
>>>>>>> upstream/main
