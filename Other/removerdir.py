'''
Remove all files and directories in current directory.
Be careful!
'''

import os
import sys

print()
dr = 0
fl = 0
def cleanDir():
    global dr, fl
    lines = os.listdir()
    for ln in lines:
        if ln == os.path.split(sys.argv[0])[1]: continue
        if not os.path.isdir(ln):
            os.remove(ln)
            print('file = '+ ln + ' <removed>')
            fl += 1
        else:
            print('Founded dir', ln)
            os.chdir(ln)
            cleanDir()
            os.chdir('..')
            os.removedirs(ln)
            dr += 1
            print('directory exited')

if input('Really do thad shit? Y/y for agree: ') in ['Y', 'y']: cleanDir()
print('[Removed = {} directories, {} files]'.format(dr, fl))
