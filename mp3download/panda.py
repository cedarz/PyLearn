# -*- coding: cp936 -*-
import urllib, urllib2, cookielib
import re
from HTMLParser import HTMLParser

udict = {}

class MyHtmlParser(HTMLParser):
    def __init__(self, _reg = r"第\d*课", _songname = "Kunfu Panda"):
        HTMLParser.__init__(self)
        self.songname = _songname
        self.text_print = False
        self.regex = re.compile(_reg)
        self.item = None
        self.urldict = {}
        self.net = 'http://www.rrting.net'
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.text_print = True
            self.item = attrs
            #print "a start tag: ", tag, "attrs: ", attrs
    def handle_endtag(self, tag):
        if tag == 'a':
            self.text_print = False
    def handle_data(self, data):
        if self.text_print :
            if(self.regex.findall(data)):
                print "data: ", data, "\nattrs: ", self.item[0][1]
                self.urldict[data] = self.net + self.item[0][1]
    def result(self):
        return self.urldict

page = urllib2.urlopen('http://www.rrting.net/English/movie_mp3/162165/').read()
#print urllib2.urlopen('http://www.rrting.net/English/EAfilms/111987/').read()
parser = MyHtmlParser()
parser.feed(page)
parser.close()
for name, urls in parser.result().items():
    print name, urls
    parser = MyHtmlParser(r"MP3下载")
    subpage = urllib2.urlopen(urls).read()
    parser.feed(subpage)
    parser.close()
