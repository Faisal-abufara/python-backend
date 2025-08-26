from threading import Thread
import time
ElTime=time.time()
X=10
Y=20
def Task1():

    print("Task 1 Starts: ")
    time.sleep(5)
    print(X+Y)
    print("Task 1 Ends")

def Task2():
    print("Task 2 Starts: ")
    print(X*Y)
    print("Task 2 Ends")

def Task3():
    print("Task 3 Starts: ")
    time.sleep(3)
    print(X-Y)
    print("Task 3 Ends")

MyThread = []
MyThread.append(Thread(target=Task1))
MyThread.append(Thread(target=Task2))
MyThread.append(Thread(target=Task3))

for i in MyThread:
    i.start()

for i in MyThread:
    i.join()