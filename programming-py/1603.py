class ParkingSystem:
    def __init__(self, big, medium, small):
        # self.big = big
        # self.medium = medium
        # self.small = small
        self.parking = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        self.parking[carType] -= 1
        return self.parking[carType] + 1 > 0
        # if carType == 1:
        #     if self.big == 0:
        #         return False
        #     self.big -= 1
        #     return True
        # elif carType == 2:
        #     if self.medium == 0:
        #         return False
        #     self.medium -= 1
        #     return True
        # else:
        #     if self.small == 0:
        #         return False
        #     self.small -= 1
        #     return True


# test below
ps1 = ParkingSystem(2, 3, 4)
print(ps1.addCar(1))
print(ps1.addCar(1))
print(ps1.addCar(1))
