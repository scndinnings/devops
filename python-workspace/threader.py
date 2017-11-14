import time
from threading import Thread

def func(i):
    fact=1
    j=i
    while(j>0):
        fact = fact * j
        j = j - 1
    print("\nSleeping for thread", i)
    time.sleep(5)
    print("\nWaking for thread",i)
    print("\nFactorial is",fact)

for i in range(1,10):
    t=Thread(target=func,args=(i,))
    t.start()
