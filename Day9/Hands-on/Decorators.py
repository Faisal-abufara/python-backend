from time import time
def Decor1 (Func):
    def howHigh():

        Start = time()

        Func()

        End = time()

        print(f"The Time To Run The Task {End - Start:.6f}")
    return howHigh

@Decor1
def BigFor():
    for Number in range(1,201):
        print(Number)


BigFor()

