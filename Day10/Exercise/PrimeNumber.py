'''
check:
if it's a positive integer greater than 1 and 
if it has exactly two factors: 1 and the number itself
'''
def _Prime(Number):
    if Number <=1:
        return False
    for i in range(2,int(Number**0.5+1)):
        if Number % i == 0:   
            return False
    return True

def MyGen():
    Number = 2
    while True:
        if _Prime(Number):
                yield Number
        Number+=1

MyGenrator = MyGen()
for i in range(20):
    print(next(MyGenrator))