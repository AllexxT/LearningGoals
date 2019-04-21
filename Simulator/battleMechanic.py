one = 10
two = 10
'''
while one > 0 and two > 0:
    print('One', one)
    print('Two', two)
    if two > 0:
        one -= 3
        if one <= 0:
            print('One', one)
            print('two is winner')
    if one > 0:
        two -= 4
        if two <= 0:
            print('Two', two)
            print('One is winner')
'''

import threading
import _thread
import time

lock = threading.Lock()

def func(arg, text):
    
    x = 0
    while x < 10:
        time.sleep(arg)
        lock.acquire()
        print(text)
        x += 1
        lock.release()


_thread.start_new_thread(func, (1, 'Griha'))
_thread.start_new_thread(func, (1.5, 'Ne Griha'))
