# -*- coding: utf-8 -*-
__author__ = 'Tom Chen'

"""
Module implementing zhuifan.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import PyQt4,sys,os,time,threading
from PyQt4 import QtCore,QtGui
from urllib import quote

from Ui_zhuifanmain import Ui_zhuifan

from weekindex import catchcode               #获取新番列表及更新时间
from zhuifanson import zhuifanson,getname
from remodel import *



default_encoding = 'utf-8'                        #设置文件使用UTF-8编码
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class zhuifan(QDialog, Ui_zhuifan):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.index01.setFlat(True)
        self.index02.setFlat(True)
        self.index03.setFlat(True)
        self.index04.setFlat(True)
        self.index05.setFlat(True)
        self.index06.setFlat(True)
        self.index07.setFlat(True)
        self.index08.setFlat(True)
        self.index09.setFlat(True)
        self.index10.setFlat(True)
        self.index11.setFlat(True)
        self.index12.setFlat(True)
        self.index13.setFlat(True)
        self.index14.setFlat(True)
        self.index15.setFlat(True)
        self.index16.setFlat(True)
        self.index17.setFlat(True)
        self.index18.setFlat(True)
        self.save01.setFlat(True)
        self.save02.setFlat(True)
        self.save03.setFlat(True)
        self.save04.setFlat(True)
        self.save05.setFlat(True)
        self.save06.setFlat(True)
        self.save07.setFlat(True)
        self.save08.setFlat(True)
        self.save09.setFlat(True)
        self.save10.setFlat(True)
        self.save11.setFlat(True)
        self.save12.setFlat(True)
        self.index01.resize(0,0)
        self.index02.resize(0,0)
        self.index03.resize(0,0)
        self.index04.resize(0,0)
        self.index05.resize(0,0)
        self.index06.resize(0,0)
        self.index07.resize(0,0)
        self.index08.resize(0,0)
        self.index09.resize(0,0)
        self.index10.resize(0,0)
        self.index11.resize(0,0)
        self.index12.resize(0,0)
        self.index13.resize(0,0)
        self.index14.resize(0,0)
        self.index15.resize(0,0)
        self.index16.resize(0,0)
        self.index17.resize(0,0)
        self.index18.resize(0,0)
        self.save01.resize(0,0)
        self.save02.resize(0,0)
        self.save03.resize(0,0)
        self.save04.resize(0,0)
        self.save05.resize(0,0)
        self.save06.resize(0,0)
        self.save07.resize(0,0)
        self.save08.resize(0,0)
        self.save09.resize(0,0)
        self.save10.resize(0,0)
        self.save11.resize(0,0)
        self.save12.resize(0,0)
        self.index = catchcode()            #获取新番列表及更新时间

        with open('savename','r') as f:
            savename = f.readline()
            savelist = savename.split(';')
            if savelist[0] == 'Bilibili':
                self.first.setCurrentIndex(0)    #设置下拉框的初始值
            else:
                self.first.setCurrentIndex(1)

        self.indextext(self.index[6])
        global N
        N = 0


    def indextext(self,listname):              #判断显示label还是隐藏
        n = len(listname)
        if n > 0:
            self.index01.resize(191,27)
            self.index01.setText(listname[0].decode('utf-8'))
        else:
            self.index01.resize(0,0)
        if n > 1:
            self.index02.resize(191,27)
            self.index02.setText(listname[1].decode('utf-8'))
        else:
            self.index02.resize(0,0)
        if n > 2:
            self.index03.resize(191,27)
            self.index03.setText(listname[2].decode('utf-8'))
        else:
            self.index03.resize(0,0)
        if n > 3:
            self.index04.resize(191,27)
            self.index04.setText(listname[3].decode('utf-8'))
        else:
            self.index04.resize(0,0)
        if n > 4:
            self.index05.resize(191,27)
            self.index05.setText(listname[4].decode('utf-8'))
        else:
            self.index05.resize(0,0)
        if n > 5:
            self.index06.resize(191,27)
            self.index06.setText(listname[5].decode('utf-8'))
        else:
            self.index06.resize(0,0)
        if n > 6:
            self.index07.resize(191,27)
            self.index07.setText(listname[6].decode('utf-8'))
        else:
            self.index07.resize(0,0)
        if n > 7:
            self.index08.resize(191,27)
            self.index08.setText(listname[7].decode('utf-8'))
        else:
            self.index08.resize(0,0)
        if n > 8:
            self.index09.resize(191,27)
            self.index09.setText(listname[8].decode('utf-8'))
        else:
            self.index09.resize(0,0)
        if n > 9:
            self.index10.resize(191,27)
            self.index10.setText(listname[9].decode('utf-8'))
        else:
            self.index10.resize(0,0)
        if n > 10:
            self.index11.resize(191,27)
            self.index11.setText(listname[10].decode('utf-8'))
        else:
            self.index11.resize(0,0)
        if n > 11:
            self.index12.resize(191,27)
            self.index12.setText(listname[11].decode('utf-8'))
        else:
            self.index12.resize(0,0)
        if n > 12:
            self.index13.resize(191,27)
            self.index13.setText(listname[12].decode('utf-8'))
        else:
            self.index13.resize(0,0)
        if n > 13:
            self.index14.resize(191,27)
            self.index14.setText(listname[13].decode('utf-8'))
        else:
            self.index14.resize(0,0)
        if n > 14:
            self.index15.resize(191,27)
            self.index15.setText(listname[14].decode('utf-8'))
        else:
            self.index15.resize(0,0)
        if n > 15:
            self.index16.resize(191,27)
            self.index16.setText(listname[15].decode('utf-8'))
        else:
            self.index16.resize(0,0)
        if n > 16:
            self.index17.resize(191,27)
            self.index17.setText(listname[16].decode('utf-8'))
        else:
            self.index17.resize(0,0)
        if n > 17:
            self.index18.resize(191,27)
            self.index18.setText(listname[17].decode('utf-8'))
        else:
            self.index18.resize(0,0)

    def savetext(self,listname):
        n = len(listname)
        if n > 1:
            self.save01.resize(191,27)
            self.save01.setText(listname[1].decode('utf-8'))
        else:
            self.save01.resize(0,0)
        if n > 2:
            self.save02.resize(191,27)
            self.save02.setText(listname[2].decode('utf-8'))
        else:
            self.save02.resize(0,0)
        if n > 3:
            self.save03.resize(191,27)
            self.save03.setText(listname[3].decode('utf-8'))
        else:
            self.save03.resize(0,0)
        if n > 4:
            self.save04.resize(191,27)
            self.save04.setText(listname[4].decode('utf-8'))
        else:
            self.save04.resize(0,0)
        if n > 5:
            self.save05.resize(191,27)
            self.save05.setText(listname[5].decode('utf-8'))
        else:
            self.save05.resize(0,0)
        if n > 6:
            self.save06.resize(191,27)
            self.save06.setText(listname[6].decode('utf-8'))
        else:
            self.save06.resize(0,0)
        if n > 7:
            self.save07.resize(191,27)
            self.save07.setText(listname[7].decode('utf-8'))
        else:
            self.save07.resize(0,0)
        if n > 8:
            self.save08.resize(191,27)
            self.save08.setText(listname[8].decode('utf-8'))
        else:
            self.save08.resize(0,0)
        if n > 9:
            self.save09.resize(191,27)
            self.save09.setText(listname[9].decode('utf-8'))
        else:
            self.save09.resize(0,0)
        if n > 10:
            self.save10.resize(191,27)
            self.save10.setText(listname[10].decode('utf-8'))
        else:
            self.save10.resize(0,0)
        if n > 11:
            self.save11.resize(191,27)
            self.save11.setText(listname[11].decode('utf-8'))
        else:
            self.save11.resize(0,0)
        if n > 12:
            self.save12.resize(191,27)
            self.save12.setText(listname[12].decode('utf-8'))
        else:
            self.save12.resize(0,0)


    def checkfirst(self):
        with open('savename','r') as f:
            savename = f.readline()
            savelist = savename.split('\n')
            savelist = savelist[0].split(';')
        if savelist[0] != self.first.currentText():
            if savelist[0] == 'Bilibili':
                savelist[0] = 'Soku'
            else:
                savelist[0] = 'Bilibili'
            savename = ';'.join(savelist)
        with open('savename','w') as f:
            f.write(savename)


    def showson(self,name,videotype):
        getname(name,videotype)
        self.zfs = zhuifanson()
        self.zfs.show()


    @pyqtSignature("")
    def on_sun_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[6])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_mon_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[0])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_tue_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[1])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_wed_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[2])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_thu_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[3])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_fri_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[4])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_sat_clicked(self):
        """
        Slot documentation goes here.
        """
        self.indextext(self.index[5])
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index01_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index01.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index02_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index02.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index03_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index03.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index04_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index04.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index05_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index05.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index06_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index06.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index07_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index07.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index08_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index08.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index09_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index09.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index10_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index10.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index11_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index11.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index12_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index12.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index13_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index13.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index14_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index14.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index15_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index15.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index16_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index16.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index17_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index17.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_index18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.index18.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_searchbtn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.searchtext.text())
        if not listname:
            self.searchtext.setText(u'输入框不能为空')
            return
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save01_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save01.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save02_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save02.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save03_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save03.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save04_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save04.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save05_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save05.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save06_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save06.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save07_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save07.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save08_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save08.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save09_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save09.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save10_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save10.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save11_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save11.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_save12_clicked(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.save12.text())
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_searchtext_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.checkfirst()
        videotype = self.first.currentText()
        listname = str(self.searchtext.text())
        if not listname:
            self.searchtext.setText(u'输入框不能为空')
            return
        listname = renum(listname)
        listname = quotename(listname)
        self.showson(listname,videotype)
        
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_historybtn_clicked(self):
        """
        Slot documentation goes here.
        """
        global N
        with open('history','r') as f:
            historylist = f.read()
            print historylist
        self.historytext.setText(historylist.decode('utf-8'))
        self.historytext.moveCursor(QtGui.QTextCursor.End)  #光标置底
        print N
        if N == 0:
            self.resize(935,593)
            N = 1
        else:
            self.resize(666,593)
            N = 0

        
        # TODO: not implemented yet
        raise NotImplementedError

    def setsavetext(self):
        while True:
            with open('savename','r') as f:
                savename = f.readline()
                savelist = savename.split('\n')
                savelist = savelist[0].split(';')
                self.savetext(savelist)
                time.sleep(1)
        


def quotename(qname):
        name = quote(qname)
        return name
        

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    zf = zhuifan()
    zf.show()
    p = threading.Thread(target=zf.setsavetext)
    p.setDaemon(True)            #子线程随主线程结束而结束
    p.start()
    sys.exit(app.exec_())
