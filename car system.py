class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"{self.brand} {self.model} has started.")
        else:
            print("Cannot start the car. Fuel tank is empty!")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped.")
        else:
            print("The car is already off.")

    def refuel(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        if self.fuel_level + amount > self.fuel_capacity:
            print("Too much fuel! Can't exceed fuel capacity.")
        else:
            self.fuel_level += amount
            print(f"Refueled {amount} liters. Current fuel: {self.fuel_level} liters.")

    def drive(self, distance):
        fuel_needed = distance * 0.56  

        if not self.is_running:
            print("Start the car first!")
            return

        if fuel_needed > self.fuel_level:
            print("Not enough fuel for the trip!")
        else:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} km. Remaining fuel: {self.fuel_level:.1f} liters.")

    def display_car_info(self):
        print("----- CAR INFO -----")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity}L")
        print(f"Fuel Level: {self.fuel_level}L")
        print(f"Running: {self.is_running}")
        
        
car1 = Car("Volkswagen", "Golf R", 2018, 50)

car1.refuel(20)
car1.start()
car1.drive(50)
car1.display_car_info()

