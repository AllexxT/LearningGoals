import time, os, sys, datetime

#for
#reworking

'''Programm for counting your time work'''

def timer():
    print('* Session is started')
    nwsess = time.time()
    log = open('log.txt', 'r')
    globl = int(log.read())
    log.close()
    print('* Global working time at this moment is: ' + str(datetime.timedelta(seconds = globl)))
    input('Press any key for end this session ')
    timeofnews = int(-float(nwsess - time.time()))
    newglobl = globl + timeofnews
    print('>> Time of this session is: ' + str(datetime.timedelta(seconds = timeofnews)))
    print('>> Global: ' + str(datetime.timedelta(seconds = newglobl)))
    open('log.txt', 'w').write(str(newglobl))

timer()
