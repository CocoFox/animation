# -*- coding: utf-8 -*-

__author__ = 'Tom Chen'

import urllib2,sys,re,time
from sgmllib import SGMLParser
from datetime import datetime,date

default_encoding = 'utf-8'                        #设置文件使用UTF-8编码
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
 

class findyouku(SGMLParser):                  #分析HTML源代码
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_a = ''
        self.url = []
        self.sonurl = []
        self.u = ''
        self.num = []
        self.is_label = ''
        self.yuan = []


    def start_a(self,attrs):
        try:
            if attrs[1][0] == 'target' and attrs[1][1] == '_blank' and attrs[0][0] == 'href':
                if attrs[2][0] == '_log_type' and attrs[2][1] == '2':
                    self.url.append(attrs[0][1])
        except IndexError:
            pass

        try:
            if attrs[1][0] == 'target' and attrs[1][1] == '_blank' and attrs[0][0] == 'href':
                    self.u = attrs[0][1]
                    self.is_a = 'sonurl'
        except IndexError:
            pass

    def end_a(self):
        self.is_a = ""

    def start_label(self,attrs):
        try:
            if attrs[0][0] == 'title' and attrs[1][0] == 'stypename':
                self.is_label = 'yuan'
        except IndexError:
            pass

    def end_label(self):
        self.is_label = ''
    
    def handle_data(self, data):
        if self.is_a == 'sonurl' and re.match(r'^\d+$',str(data)):
            self.num.append(data)
            self.sonurl.append(self.u)
        if self.is_label == 'yuan':
            self.yuan.append(data)
            

def youku(sname):
    name = sname
    url = 'http://www.soku.com/v?keyword='+name
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'       #伪装浏览器请求数据
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(request).read()
    listname = findyouku()
    listname.feed(content)


    try:
        url = 'http://www.soku.com'+listname.url[0]
    except IndexError:
        return []
    request = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(request).read()
    listname = findyouku()
    listname.feed(content)
    lenyuan = len(listname.yuan)
    lennum = len(listname.num)
    newnum = []
    newsonurl = []
    if lenyuan <= 1 or lenyuan > 5:
        newnum = listname.num
        newsonurl = listname.sonurl
    elif lenyuan == 2:
        lennum = lennum + lennum%2
        newnum = listname.num[0:(lennum/2)]
        newsonurl = listname.sonurl[0:(lennum/2)]
    elif lenyuan == 3:
        if lennum % 3 != 0:
            lennum = lennum + (3 - lennum%3)
        newnum = listname.num[0:(lennum/3)]
        newsonurl = listname.sonurl[0:(lennum/3)]
    elif lenyuan == 4:
        if lennum % 4 != 0:
            lennum = lennum + (4 - lennum%4)
        newnum = listname.num[0:(lennum/4)]
        newsonurl = listname.sonurl[0:(lennum/4)]
    elif lenyuan == 5:
        if lennum % 5 != 0:
            lennum = lennum + (5 - lennum%5)
        newnum = listname.num[0:(lennum/5)]
        newsonurl = listname.sonurl[0:(lennum/5)]
    dname = []
    b = 0
    for a in newnum:
        a = int(a)
        l = [a,newsonurl[b]]
        dname.append(l)
        b = b + 1
    return dname




if __name__ == '__main__':
    youku()