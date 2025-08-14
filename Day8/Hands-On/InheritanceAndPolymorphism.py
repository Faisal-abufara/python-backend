class Cars:
    def __init__(self, Name, Color, Model, Speed):
        self.__Name = Name
        self.Color = Color
        self.Model = Model
        self.Speed = Speed

    @property
    def Name(self):
        return self.__Name

    def __str__(self):
        return f"Car Name: {self.Name}\nColor: {self.Color}\nModel: {self.Model}\nSpeed: {self.Speed} mph"

    def __repr__(self):
        return f"Cars(Name='{self.Name}', Color='{self.Color}', Model={self.Model}, Speed={self.Speed})"


my_car = Cars("Ford", "Black", 2025, 350)
print(str(my_car))
print(repr(my_car))



class Ford(Cars):
    def __init__(self, Name, Color, Model, Speed, Distance, Time):
        super().__init__(Name, Color, Model, Speed)
        self.Distance = Distance
        self.Time = Time

    def MilesPerHour(self):
        if self.Time == 0:
            return "Time cannot be zero."
        return self.Distance / self.Time

    def __str__(self):
        base_str = super().__str__()
        mph = self.MilesPerHour()
        return f"{base_str}\nCalculated Speed: {mph:.2f} mph"

    def __repr__(self):
        
        return (f"Ford(Name='{self.Name}', Color='{self.Color}', Model={self.Model}, "
                f"Speed={self.Speed}, Distance={self.Distance}, Time={self.Time})")


my_car = Cars("Ford", "Black", 2025, 350)
print(str(my_car))  
print(repr(my_car))   
print("="*30)

my_ford = Ford("Mustang", "Red", 2025, 350, 200, 4)
print(str(my_ford))   
print(repr(my_ford))  