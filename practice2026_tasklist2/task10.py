class SafeCar:
    def init(self, mileage):
        self._mileage = mileage

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self._mileage = value
