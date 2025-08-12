class Person:
    def __init__(self,Name="Suspect", Age=0):
        self.Name = Name
        self.Age = Age
    def Interdouce(self):
        print(f"My Name is: {self.Name}, My Age is :{self.Age}")

P1 = Person("Faisal",26)
P1.Interdouce()

P2 = Person()
P2.Interdouce()

P3 = Person("Nour", 23)
P3.Interdouce()