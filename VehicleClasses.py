import random


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    def getMaintenanceStatus(self):
        return self.NeedsMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

    def tripStarted(self):
        self.TripsSinceMaintenance += 1
        if self.TripsSinceMaintenance >= 100:
            self.NeedsMaintenance = True

    def repair(self):
        if self.NeedsMaintenance:
            self.TripsSinceMaintenance = 0
            self.NeedsMaintenance = False
            return True
        else:
            return False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):
        if not self.isDriving:
            self.isDriving = True
            return True
        else:
            return False

    def Stop(self):
        if self.isDriving:
            self.isDriving = False
            self.tripStarted()
            return True
        else:
            return False

    def __str__(self):
        return "The car is " + self.make + " " + self.model + " from year " + str(self.year) + " and weights " + str(
            self.weight) + "\nCurrently has been driven " + str(
            self.TripsSinceMaintenance) + " times and " + (
                   "needs " if self.NeedsMaintenance else " doesn't need ") + "maintenance.\n"


class Plane(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False

    def Fly(self):
        if not self.getMaintenanceStatus():
            if not self.isFlying:
                self.isFlying = True
                return True
            else:
                return False
        else:
            print("Plane needs to be repaired before flying again.")

    def Land(self):
        if self.isFlying:
            self.isFlying = False
            self.tripStarted()
            return True
        else:
            return False

    def __str__(self):
        return "The plane is " + self.make + " " + self.model + " from year " + str(self.year) + " and weights " + str(
            self.weight) + "\nCurrently has been driven " + str(
            self.TripsSinceMaintenance) + " times and " + (
                   "needs " if self.NeedsMaintenance else " doesn't need ") + "maintenance.\n"


newCar1 = Cars("Mercedes", "C-Class", 2020, 1561)
newCar2 = Cars("Tesla", "Model S", 2017, 1961)
newCar3 = Cars("VW", "Jetta", 2020, 1950)
newPlane1 = Plane("Boeing", "777-200LR", 2018, 223168)

for i in range(random.randrange(300)):
    newCar1.Drive()
    newCar1.Stop()

for i in range(random.randrange(300)):
    newCar2.Drive()
    newCar2.Stop()

for i in range(random.randrange(300)):
    newCar3.Drive()
    newCar3.Stop()

for i in range(random.randrange(300)):
    newPlane1.Fly()
    newPlane1.Land()


print(newCar1)
print(newCar2)
print(newCar3)
print(newPlane1)
