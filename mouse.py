# -*- coding:utf-8 -*-
import time,win32gui,win32api,win32con
from ctypes import *


def get_curpos():
    return win32gui.GetCursorPos()  #抓取鼠标当前位置


def main():
    n = raw_input('enter time in second:')
    print '10 seconds countdown'
    for a in range(10):
        print '%ds' %(10-a)
        time.sleep(1)
    for b in range(int(n)*50):
        pos=get_curpos()
        print pos[0],pos[1]
        time.sleep(0.01)
        windll.user32.SetCursorPos(pos[0],pos[1])             #设定鼠标位置
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)    #按下鼠标左键
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   #松开鼠标左键


if __name__=='__main__':
    main()