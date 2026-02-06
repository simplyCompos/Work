class Car:
    def init(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km

    def info(self):
        print(self)

    def str(self):
        return f"{self.brand}, {self.year}, mileage: {self.mileage} km"
