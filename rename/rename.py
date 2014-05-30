import os
import sys
import re


def fk(filename, src, dst):
    strinfo = re.compile(src)
    return strinfo.sub(dst, filename)

def get_input(str):
    while(True):
        path = raw_input(str)
        if path is None:
            print "The Directory can't be Null"
        else:
            break
    return path

def Main():
    
    path = get_input("Path>>>")
    src = get_input("SubstringToSubstitute>>>")
    dst = get_input("SubstringSubstituteTo>>>")

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

