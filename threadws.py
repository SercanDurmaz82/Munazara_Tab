from threading import Thread
from time import sleep

def wait():
    sleep(5)
    print("5 saniye")
x = Thread(target=wait)
x.start()
sleep(4)
print("4 saniye")
