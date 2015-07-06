# -*- coding: utf-8 -*-

__author__ = 'Tom Chen'

import urllib2,sys,re,time
from sgmllib import SGMLParser
from urllib import unquote
from datetime import datetime,date

default_encoding = 'utf-8'                        #设置文件使用UTF-8编码
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
 

class WeekIndex(SGMLParser):                  #分析HTML源代码
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_td = ''
        self.indextime = []
        self.indexname = []


    def start_td(self,attrs):
        if attrs != []:
            if attrs[0][0] == 'width' and attrs[0][1] == '130':
                self.is_td = 'time'
            if attrs[0][0] == 'width' and attrs[0][1] == '200':
                self.is_td = 'name'

    def end_td(self):
        self.is_td = ""

    
    def handle_data(self, data):
        if self.is_td == 'time' and re.match(r'^\d',data):
            self.indextime.append(data)
        if self.is_td == 'name':
            self.indexname.append(data)
        

def catchcode():
    l = time.strftime("%Y-%m-%d %A %X %Z", time.localtime())      #获取本地时间
    year = str(int(l[0])*1000+int(l[1])*100+int(l[2])*10+int(l[3]))
    month = int(l[5])*10+int(l[6])
    if month < 4:                                          #计算应该获取几月新番列表
        strmonth = '01'
    elif month < 7:
        strmonth = '04'
    elif month < 10:
        strmonth = '07'
    else:
        strmonth = '10'
    url = 'http://www.xydm.net/cartoon/'+year+'/'+year+strmonth+'/index.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'       #伪装浏览器请求数据
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(request).read()
    weekindex = WeekIndex()
    weekindex.feed(content)
    strindextime = []
    indexdate = []
    index = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for s in range(len(weekindex.indextime)):
        strindextime.append(unquote(weekindex.indextime[s]))
        l = strindextime[s].split('\xe5\xb9\xb4')
        y = l[0]
        l = l[1].split('\xe6\x9c\x88')
        m = l[0]
        l = l[1].split('\xe6\x97\xa5')
        d = l[0]
        n = date(int(y),int(m),int(d))
        indexdate.append(n.weekday())          #获取新番周几更新

    for b in range(len(weekindex.indexname)-1):
        index[indexdate[b]].append(weekindex.indexname[b+1])

    return index          #返回index字典{[周一更新...],[周二更新...],...}




if __name__ == '__main__':
    print catchcode()