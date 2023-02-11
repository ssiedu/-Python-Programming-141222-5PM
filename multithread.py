from threading import Thread
import time
class First(Thread):
    def run(self):
        for i in range(5):
            print("cube is : ",i*i*i)
            time.sleep(0.3)
class Second(Thread):
    def run(self):
        for i in range(5):
            print("Square of a number : ",i*i)
            time.sleep(0.3)


t1=First()
t2=Second()
t1.start()
time.sleep(0.3)
t2.start()
t1.join()
t2.join()
print("Bye")
