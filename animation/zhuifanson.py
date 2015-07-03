# -*- coding: utf-8 -*-

"""
Module implementing zhuifanson.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import PyQt4,sys,webbrowser,time,threading
from PyQt4 import QtCore,QtGui
from urllib import unquote

from Ui_zhuifanson import Ui_sontitle

from findyouku import youku
from findbilibili import bilibili
from downloads import downloadvideo

def getname(listname,videotype):
    global NAME,VIDEOTYPE
    NAME = listname
    VIDEOTYPE = videotype

class zhuifanson(QDialog, Ui_sontitle):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        global NAME,VIDEOTYPE,NUM
        QDialog.__init__(self, parent)
        NUM = 0
        self.setupUi(self)
        self.name = NAME
        unquotename = unquote(self.name)
        self.sonname.setText(u'%s'%unquotename)
        self.sonname.setFont(QFont("Roman times",20,QFont.Bold))
        self.setWindowTitle(u'%s'%unquotename)
        videotype = VIDEOTYPE
        if videotype == 'Soku':
            #youku
            self.dname = youku(self.name)
            self.n = len(self.dname)
            if self.n == 0:
                self.dname = bilibili(self.name)
                self.n = len(self.dname)

        if videotype == 'Bilibili':
            #bilibili
            self.dname = bilibili(self.name)
            self.n = len(self.dname)
            if self.n == 0:
                self.dname = youku(self.name)
                self.n = len(self.dname)

        with open('savename','r') as f:
            savename = f.readline()
            savelist = savename.split('\n')
            savelist = savelist[0].split(';')
            if unquotename in savelist:
                self.savebtn.setText(u'已收藏')
            else:
                self.savebtn.setText(u'收藏')

        
        self.son01.setFlat(True)
        self.son02.setFlat(True)
        self.son03.setFlat(True)
        self.son04.setFlat(True)
        self.son05.setFlat(True)
        self.son06.setFlat(True)
        self.son07.setFlat(True)
        self.son08.setFlat(True)
        self.son09.setFlat(True)
        self.son10.setFlat(True)
        self.son11.setFlat(True)
        self.son12.setFlat(True)
        self.son13.setFlat(True)

        if self.n > 0:
            self.son01.resize(98,27)
            self.son01.setText(u'第%s集'%self.dname[self.n-1][0])
        else:
            self.son01.resize(0,0)
        if self.n > 1:
            self.son02.resize(98,27)
            self.son02.setText(u'第%s集'%self.dname[self.n-2][0])
        else:
            self.son02.resize(0,0)
        if self.n > 2:
            self.son03.resize(98,27)
            self.son03.setText(u'第%s集'%self.dname[self.n-3][0])
        else:
            self.son03.resize(0,0)
        if self.n > 3:
            self.son04.resize(98,27)
            self.son04.setText(u'第%s集'%self.dname[self.n-4][0])
        else:
            self.son04.resize(0,0)
        if self.n > 4:
            self.son05.resize(98,27)
            self.son05.setText(u'第%s集'%self.dname[self.n-5][0])
        else:
            self.son05.resize(0,0)
        if self.n > 5:
            self.son06.resize(98,27)
            self.son06.setText(u'第%s集'%self.dname[self.n-6][0])
        else:
            self.son06.resize(0,0)
        if self.n > 6:
            self.son07.resize(98,27)
            self.son07.setText(u'第%s集'%self.dname[self.n-7][0])
        else:
            self.son07.resize(0,0)
        if self.n > 7:
            self.son08.resize(98,27)
            self.son08.setText(u'第%s集'%self.dname[self.n-8][0])
        else:
            self.son08.resize(0,0)
        if self.n > 8:
            self.son09.resize(98,27)
            self.son09.setText(u'第%s集'%self.dname[self.n-9][0])
        else:
            self.son09.resize(0,0)
        if self.n > 9:
            self.son10.resize(98,27)
            self.son10.setText(u'第%s集'%self.dname[self.n-10][0])
        else:
            self.son10.resize(0,0)
        if self.n > 10:
            self.son11.resize(98,27)
            self.son11.setText(u'第%s集'%self.dname[self.n-11][0])
        else:
            self.son11.resize(0,0)
        if self.n > 11:
            self.son12.resize(98,27)
            self.son12.setText(u'第%s集'%self.dname[self.n-12][0])
        else:
            self.son12.resize(0,0)
        if self.n > 12:
            self.son13.resize(98,27)
            self.son13.setText(u'第%s集'%self.dname[self.n-13][0])
        else:
            self.son13.resize(0,0)
    
    @pyqtSignature("")
    def on_son01_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-1][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son02_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-2][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son03_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-3][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son04_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-4][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son05_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-5][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son06_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-6][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son07_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-7][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son08_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-8][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son09_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-9][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son10_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-10][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son11_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-11][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son12_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-12][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_son13_clicked(self):
        """
        Slot documentation goes here.
        """
        webbrowser.open(self.dname[self.n-13][1])
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_savebtn_clicked(self):
        """
        Slot documentation goes here.
        """
        global NAME
        name = unquote(NAME)
        with open('savename','r') as f:
            savename = f.readline()
            savelist = savename.split('\n')
            savelist = savelist[0].split(';')
        if self.savebtn.text() == u'收藏':
            savelist.append(name)
            self.savebtn.setText(u'已收藏')
        else:
            n = len(savelist)-1
            for a in range(n):
                if savelist[a+1] == name:
                    savelist.pop(a+1)
                    break
            self.savebtn.setText(u'收藏')
        with open('savename','w') as f:
            savename = ';'.join(savelist)
            f.write(savename)


        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_downloadbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        global NUM
        names = locals()
        NUM = NUM + 1
        names['p%d'%NUM] = threading.Thread(target=self.download)   #动态命名变量名
        names['p%d'%NUM].setDaemon(True)            #子线程随主线程结束而结束
        names['p%d'%NUM].start()
        # TODO: not implemented yet
        raise NotImplementedError

    def download(self):
        startnum = self.startnum.text()
        endnum = self.endnum.text()
        name = unquote(NAME)
        if startnum == '':
            startnum = self.dname[self.n-13][0]
        if endnum == '':
            endnum = self.dname[self.n-1][0]
        downloadlist = []
        for a in range(int(startnum),int(endnum)+1):
            self.loginfo.append('>start download %dth of (%s to %s)<\n' %(a,startnum,endnum))
            self.loginfo.append('downloading %dth,please wait......\n' %a)
            QApplication.processEvents()           #立即显示输出的内容
            self.loginfo.moveCursor(QtGui.QTextCursor.End)  #光标置底
            downloadvideo(a,self.dname[a-1][1],name)
            self.loginfo.append('>%dth was downloaded<\n' %a)
            self.loginfo.moveCursor(QtGui.QTextCursor.End)


if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    zfs = zhuifanson()
    zfs.show()
    sys.exit(app.exec_())
