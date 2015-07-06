#-*- coding:utf-8 -*-
from urllib import unquote,quote
import re

name = 'Punch Line'
name = unquote(name)
l = name.split(' ')
m = []
s = ''
rename = re.compile('第')
if len(l) != 1:
    s = l[len(l)-1]
    if rename.findall(s):
        m = name.split(s)
    else:
        m.append(name) 
else:
    m.append(name)
m[0] = quote(m[0])
print unquote(m[0])
