#-*- coding:utf-8 -*-
import urllib2,sys,re,urllib,os
from sgmllib import SGMLParser
from datetime import datetime,date
 

class downloads(SGMLParser):                  #分析HTML源代码
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_a = ''
        self.url = []

    def start_a(self,attrs):
        try:
            if attrs[0][0] == 'href' and attrs[1][1] == '_blank' and attrs[1][0] == 'target':
                if attrs[2][0] == 'class' and attrs[2][1] == 'link':
                    self.url.append(attrs[0][1])
        except IndexError:
            pass
        try:
            if attrs[0][0] == 'href' and attrs[1][1] == '_blank' and attrs[1][0] == 'target':
                if attrs[2][0] == 'onclick':
                    self.url.append(attrs[0][1])
        except IndexError:
            pass
    def end_a(self):
        pass

    def handle_data(self, data):
        pass

def downloadvideo(num,url,name):
    videourl = url
    url = 'http://www.flvcd.com/parse.php?kw=' + videourl + '&flag=one&format=super'
     
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'       #伪装浏览器请求数据
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(request).read()
    downloadurl = downloads()
    downloadurl.feed(content)
    name = unicode(name, 'utf8')
    if os.path.exists(name):
        pass
    else:
        os.mkdir(name)
    n = 0
    print '>start download '+name+str(num)+'<'
    for a in downloadurl.url:
        n = n + 1
        print '>downloading %d part of %d part(s)<' %(n,len(downloadurl.url))
        urllib.urlretrieve(a, name + '/' + name + str(num) +'part'+str(n)+'.flv')
        print '>downloaded %d part of %d part(s)<' %(n,len(downloadurl.url))
    print '>download '+name+str(num)+'is done<'


if __name__ == '__main__':
    downloadvideo()
