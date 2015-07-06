# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/chenweidong/zhuifan/zhuifanson.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sontitle(object):
    def setupUi(self, sontitle):
        sontitle.setObjectName(_fromUtf8("sontitle"))
        sontitle.resize(603, 480)
        sontitle.setMouseTracking(False)
        self.sonname = QtGui.QLabel(sontitle)
        self.sonname.setGeometry(QtCore.QRect(30, 30, 441, 51))
        self.sonname.setIndent(-3)
        self.sonname.setObjectName(_fromUtf8("sonname"))
        self.textBrowser = QtGui.QTextBrowser(sontitle)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 561, 171))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.savebtn = QtGui.QPushButton(sontitle)
        self.savebtn.setEnabled(True)
        self.savebtn.setGeometry(QtCore.QRect(480, 40, 101, 27))
        self.savebtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.savebtn.setMouseTracking(False)
        self.savebtn.setIconSize(QtCore.QSize(16, 16))
        self.savebtn.setObjectName(_fromUtf8("savebtn"))
        self.son01 = QtGui.QPushButton(sontitle)
        self.son01.setGeometry(QtCore.QRect(30, 100, 98, 27))
        self.son01.setObjectName(_fromUtf8("son01"))
        self.son02 = QtGui.QPushButton(sontitle)
        self.son02.setGeometry(QtCore.QRect(140, 100, 98, 27))
        self.son02.setObjectName(_fromUtf8("son02"))
        self.son03 = QtGui.QPushButton(sontitle)
        self.son03.setGeometry(QtCore.QRect(250, 100, 98, 27))
        self.son03.setObjectName(_fromUtf8("son03"))
        self.son04 = QtGui.QPushButton(sontitle)
        self.son04.setGeometry(QtCore.QRect(360, 100, 98, 27))
        self.son04.setObjectName(_fromUtf8("son04"))
        self.son05 = QtGui.QPushButton(sontitle)
        self.son05.setGeometry(QtCore.QRect(470, 100, 98, 27))
        self.son05.setObjectName(_fromUtf8("son05"))
        self.son06 = QtGui.QPushButton(sontitle)
        self.son06.setGeometry(QtCore.QRect(30, 150, 98, 27))
        self.son06.setObjectName(_fromUtf8("son06"))
        self.son08 = QtGui.QPushButton(sontitle)
        self.son08.setGeometry(QtCore.QRect(250, 150, 98, 27))
        self.son08.setObjectName(_fromUtf8("son08"))
        self.son07 = QtGui.QPushButton(sontitle)
        self.son07.setGeometry(QtCore.QRect(140, 150, 98, 27))
        self.son07.setObjectName(_fromUtf8("son07"))
        self.son09 = QtGui.QPushButton(sontitle)
        self.son09.setGeometry(QtCore.QRect(360, 150, 98, 27))
        self.son09.setObjectName(_fromUtf8("son09"))
        self.son10 = QtGui.QPushButton(sontitle)
        self.son10.setGeometry(QtCore.QRect(470, 150, 98, 27))
        self.son10.setObjectName(_fromUtf8("son10"))
        self.son13 = QtGui.QPushButton(sontitle)
        self.son13.setGeometry(QtCore.QRect(250, 200, 98, 27))
        self.son13.setObjectName(_fromUtf8("son13"))
        self.son12 = QtGui.QPushButton(sontitle)
        self.son12.setGeometry(QtCore.QRect(140, 200, 98, 27))
        self.son12.setObjectName(_fromUtf8("son12"))
        self.son11 = QtGui.QPushButton(sontitle)
        self.son11.setGeometry(QtCore.QRect(30, 200, 98, 27))
        self.son11.setObjectName(_fromUtf8("son11"))
        self.downloadbtn = QtGui.QPushButton(sontitle)
        self.downloadbtn.setGeometry(QtCore.QRect(150, 270, 98, 27))
        self.downloadbtn.setObjectName(_fromUtf8("downloadbtn"))
        self.startnum = QtGui.QLineEdit(sontitle)
        self.startnum.setGeometry(QtCore.QRect(20, 270, 41, 27))
        self.startnum.setObjectName(_fromUtf8("startnum"))
        self.endnum = QtGui.QLineEdit(sontitle)
        self.endnum.setGeometry(QtCore.QRect(100, 270, 41, 27))
        self.endnum.setObjectName(_fromUtf8("endnum"))
        self.label = QtGui.QLabel(sontitle)
        self.label.setGeometry(QtCore.QRect(70, 270, 21, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.loginfo = QtGui.QTextBrowser(sontitle)
        self.loginfo.setGeometry(QtCore.QRect(20, 300, 561, 171))
        self.loginfo.setObjectName(_fromUtf8("loginfo"))

        self.retranslateUi(sontitle)
        QtCore.QMetaObject.connectSlotsByName(sontitle)

    def retranslateUi(self, sontitle):
        sontitle.setWindowTitle(_translate("sontitle", "Dialog", None))
        self.sonname.setText(_translate("sontitle", "<html><head/><body><p><span style=\" font-size:20pt;\">text</span></p></body></html>", None))
        self.savebtn.setText(_translate("sontitle", "收藏", None))
        self.son01.setText(_translate("sontitle", "PushButton", None))
        self.son02.setText(_translate("sontitle", "PushButton", None))
        self.son03.setText(_translate("sontitle", "PushButton", None))
        self.son04.setText(_translate("sontitle", "PushButton", None))
        self.son05.setText(_translate("sontitle", "PushButton", None))
        self.son06.setText(_translate("sontitle", "PushButton", None))
        self.son08.setText(_translate("sontitle", "PushButton", None))
        self.son07.setText(_translate("sontitle", "PushButton", None))
        self.son09.setText(_translate("sontitle", "PushButton", None))
        self.son10.setText(_translate("sontitle", "PushButton", None))
        self.son13.setText(_translate("sontitle", "PushButton", None))
        self.son12.setText(_translate("sontitle", "PushButton", None))
        self.son11.setText(_translate("sontitle", "PushButton", None))
        self.downloadbtn.setText(_translate("sontitle", "下载", None))
        self.label.setText(_translate("sontitle", "<html><head/><body><p><span style=\" font-size:12pt;\">至</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sontitle = QtGui.QDialog()
    ui = Ui_sontitle()
    ui.setupUi(sontitle)
    sontitle.show()
    sys.exit(app.exec_())

