class FuelDispenser:
    def __init__(self, max_volume, price_per_liter):
        self.max_volume = max_volume          
        self.fuel_balance = max_volume        
        self.cars_served = 0                  
        self.price_per_liter = price_per_liter
        self.total_sold = 0                   

    @classmethod
    def copy(cls, other):
        new_obj = cls(other.max_volume, other.price_per_liter)
        new_obj.fuel_balance = other.fuel_balance
        new_obj.cars_served = other.cars_served
        new_obj.total_sold = other.total_sold
        return new_obj

    def refuel_car(self, liters):
        if liters <= 0:
            print("Incorrect amount of fuel")
            return

        if self.fuel_balance >= liters:
            self.fuel_balance -= liters
            self.total_sold += liters
            self.cars_served += 1
            cost = liters * self.price_per_liter
            print(f"Filled {liters} L. Price: {cost}") 
        else:
            print("Not enough fuel in the tank")

    def refill(self, liters):
        if liters <= 0:
            print("Incorrect quantity")
            return

        if self.fuel_balance + liters <= self.max_volume:
            self.fuel_balance += liters
            print(f"Added {liters} liters of fuel")
        else:
            print("Exceeding maximum volume")

    def get_report(self):
        total_money = self.total_sold * self.price_per_liter
        print("Report:")
        print(f"Earned: {total_money}")
        print(f"Fuel sold: {self.total_sold} L")
        print(f"Number of cars served: {self.cars_served}")
