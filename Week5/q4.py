"""
Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

Features:
"make" (Brand of vehicle)
"model" (Vehicle model)
"year" (Year of manufacture of the vehicle)
Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
Create an instance of each class, determine its properties, and write a program to display these properties.
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

if __name__ == "__main__":
    off_road_vehicle = OffRoadVehicle("Jeep", "Grand Cherokee", 2022, True)
    sports_car = SportsCar("Ford", "Mustang", 1969, 250)
    print("----------------------------------")
    print(f"Off-Road Vehicle - Make: {off_road_vehicle.make}, Model: {off_road_vehicle.model}, Year: {off_road_vehicle.year}, Four-Wheel Drive: {off_road_vehicle.four_wheel_drive}")
    print(f"Sports Car - Make: {sports_car.make}, Model: {sports_car.model}, Year: {sports_car.year}, Max Speed: {sports_car.max_speed} km/h")
    print("----------------------------------")
    input()