# -*- coding: cp936 -*-
import zipfile, os
import tempfile

class epubfile:
    '''
    A class of the name of epubfile, is used to substitute the old-not-compatible
    css style file(.css file) with a new one.
    This version can only work in the current work directory, that is the target
    epub files must be under the same directory as the this script.
    '''
       
    def __init__(self, path):
        self.path = path
        self.zip  = zipfile.ZipFile(path, "a")
        self.remove("temp.epub")
        self.temp = zipfile.ZipFile("temp.epub", "a", zipfile.ZIP_DEFLATED)
        self.tmp_file_name = "none.tmp"
        self.temp_zip_name = "temp.epub"
        
        
    def convert(self, style_css):
        nl =  self.zip.namelist()
        for fn in nl:
            print fn
            self.mid_file  = open("none.tmp", "w")
            templist = self.temp.namelist()
            
            if(fn.find(".css") != -1):
                if(fn not in templist):
                    self.temp.write(style_css, fn)
                    self.mid_file.close()
            else:
                #print self.zip.read(fn)
                if(fn not in templist and fn[-1] != '/'):
                    self.mid_file.write(self.zip.read(fn))
                    self.mid_file.close()
                    self.temp.write(self.tmp_file_name, fn, zipfile.ZIP_DEFLATED)
            '''
            if(fn.find("mimetype") != -1):
                s = self.zip.read(fn)
                print s
                self.mid_file.write(s)
            '''
            
            

    def rename(self):
        pwd = os.getcwd()
        self.zip.close()
        self.temp.close()
        name_tmp = os.path.join(pwd, "nothing.epub")
        sourcefile = os.path.join(pwd, self.path)
        destfile   = os.path.join(pwd, self.temp_zip_name)
        os.rename(sourcefile, name_tmp)
        os.rename(destfile, sourcefile)
        os.rename(name_tmp, destfile)
        
    def remove(self, name):
        targetfile = os.path.join(os.getcwd(), name)
        if(os.path.isfile(targetfile)):
           os.remove(targetfile)
           
    def clean(self):
        self.remove(self.tmp_file_name)
        self.remove(self.temp_zip_name)
        
    
def task_Main(afile):
    print "###" + afile + "###"
    epub = epubfile(afile)
    epub.convert("stylesheet.css")
    epub.rename()
    epub.clean()

def Main(path = os.getcwd()):
    listfile = os.listdir(path)
    for afile in listfile:
        if(afile.find(".epub") != -1):
            task_Main(afile)

if __name__ == '__main__':
    Main()


        
