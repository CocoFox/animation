# -*- coding: utf-8 -*-
import re

def renum(listname):
    name = listname
    rename = re.compile(r'\d+期$')
    a = rename.findall(name)
    if a:
        if a[0] == '1期':
            newname = name.replace(a[0],'一季')
        elif a[0] == '2期':
            newname = name.replace(a[0],'二季')
        elif a[0] == '3期':
            newname = name.replace(a[0],'三季')
        elif a[0] == '4期':
            newname = name.replace(a[0],'四季')
        elif a[0] == '5期':
            newname = name.replace(a[0],'五季')
        elif a[0] == '6期':
            newname = name.replace(a[0],'六季')
        elif a[0] == '7期':
            newname = name.replace(a[0],'七季')
        elif a[0] == '8期':
            newname = name.replace(a[0],'八季')
        elif a[0] == '9期':
            newname = name.replace(a[0],'九季')
        elif a[0] == '10期':
            newname = name.replace(a[0],'十季')
        else:
            newname = name.replace('期','季')
    else:
        newname = name

    return newname

if __name__ == '__main__':
    renum()
