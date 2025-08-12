class Car:
    def __init__(self, Name="Unknown", Color="Not specified", Model="Unknown", Year=0):
        self.Name = Name
        self.Color = Color
        self.Model = Model
        self.Year = Year

    def printinfo(self):
        print(f"Car Name: {self.Name}, Color: {self.Color}, Model: {self.Model}, Year: {self.Year}")

Car1 = Car("Ford", 'Blue', "Mustang", 2025)
Car2 = Car()

Car1.printinfo()
print("-=-" * 15)
Car2.printinfo()
