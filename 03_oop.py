# OOP (Object Oriented Programming) (https://www.youtube.com/watch?v=6soT3DMBJGQ)
class Car:                                              # Capital naming convention used in class Naming
    
    total_car = 0
    
    def __init__(self, user_brand, user_model):           # This is constructor (__init__())
        self.__brand = user_brand                        # __(double underscore is used to make it private)
        self.__model = user_model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + ' 🚕'

    def car_info(self): 
        return f"{self.__brand} ({self.__model})"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    def get_quantity(self):
        return f"Quantity: ${self.quantity}"
    
    @staticmethod                                       # to define method static we use this (also called as decoraters)
    def about_car():                                    # Static car info function
        return "Car has generally 4 tyres, work on deisel, petrol, electric also"
    
    @property                                           # To prevent it from overriding
    def get_model(self):
        return f"{self.__model}"

# my_car = Car("BMW", "M4")                             # Standard way to create objects in python
# print(my_car.brand)                                   # Accessing attributes outside class
# print(my_car.model)         
# print(my_car.car_info())                              # Accessing functions/methods outside class 


# Task2: Inheritance (Single Inheritance)
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_electric_car = ElectricCar("BYD", "Amaze", "85kWH")
# # print(my_electric_car.__brand)                        # It will give error as now __brand is now a private thing
# print(my_electric_car.get_brand())

# # Task3: Polymorphism
# hyundai = Car("Hyundai", "Verna")                       # Creating a instance of petrol or diesel car 
# print(hyundai.fuel_type())                              # Creating a instance of petrol or diesel car 

# tesla_ev = ElectricCar("Tesla", "Y", "95kWH")           # Creating a instance of electric car 
# print(tesla_ev.fuel_type())                             # Accessing the fuel type electric car object


# print(Car.total_car)                                    # To access total car variable  
# print(Car.about_car())                                  # Decorator Example
# print(hyundai.get_model)                                # Accessing function as attribute not as model using @property decorator

# print(isinstance(tesla_ev, ElectricCar))                # To check, if it is a instance of the class (Inheritance Class also return true when checked)
# print(isinstance(tesla_ev, Car))



# Multiple Inheritance
class Battery:
    # def __init__(self, battery_size):
    #     self.battery_size = battery_size

    def battery(self):
        return "This is a battery param"
    
    def cal(self):
        return "This is a cal 12"

class Engine:
    # def __init__(self, fuel_capacity):
    #     self.fuel_capacity = fuel_capacity
    
    def engine(self):
        return "This is engine param"
    
    def cal(self):
        return "This is also a cal"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_byd = ElectricCarTwo("BYD", "V12")
print(my_new_byd.cal())                                    # Call first pass class in inheritance (uses MRO (Method Resolution Order) with C3 Linearization algorithm) 