
MyString= "Faisal abufara"


MyItro=iter(MyString)


for i in MyItro:
    print(i)

MyList = [5,4,8,9,12]

MyIT = iter(MyList)

print("outside loop:")
print(next(MyIT))
print(next(MyIT))
print(next(MyIT))
print("form loop: ")
for i in MyIT:
    print(i)

#This is Iteration
class Countto:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num
        
counter = Countto(5)
for num in counter:
    print(num)

print("$$"*50)
#This is Generator

def count_up_to(max):
    current = 1
    while current <= max:
        yield current
        current += 1


for num in count_up_to(5):
    print(num)
