'''
This is a python script to rename the name of the files under the same directory.
But the present version is that intellignet. It just can substitute the common
substring in the names with another common string.
'''
import os
import sys
import re


def fk(filename, src, dst):
    strinfo = re.compile(src)
    return strinfo.sub(dst, filename)

def get_input(str):
    '''Get the directory and the substrings'''
    while(True):
        path = raw_input(str)
        if not path:
            print "The Directory can't be Null"
        else:
            break
    return path

def Main():
    
    path = get_input("Path>>>")
    src = get_input("SubstringToSubstitute>>>")
    dst = raw_input("SubstringSubstituteTo>>>")

    listfile = os.listdir(path)
    os.chdir(path)
    pwd = os.getcwd()
    #print os.getcwd()

    for iname in listfile:
        #print fk(iname, src, dst)
        print os.path.join(pwd, iname)
        if os.path.isfile(os.path.join(pwd, iname)) == True:
            os.rename(os.path.join(pwd, iname), os.path.join(pwd, fk(iname, src, dst)))

if __name__ == '__main__':
    Main()

