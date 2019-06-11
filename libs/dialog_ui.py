# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(225, 222)
        Dialog.setStyleSheet(_fromUtf8("QLineEdit { \n"
"  padding: 6px 12px;\n"
"  font-size: 14px;\n"
"  color: #555;\n"
"  background-color: #fff;\n"
"  border: 1px solid #ccc;\n"
"  border-radius: 4px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border-color: #66afe9;\n"
"}"))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.subscriptionkey = QtWidgets.QLineEdit(Dialog)
        self.subscriptionkey.setObjectName(_fromUtf8("subscriptionkey"))
        self.verticalLayout.addWidget(self.subscriptionkey)
        self.imagefolder = QtWidgets.QLineEdit(Dialog)
        self.imagefolder.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.imagefolder.setObjectName(_fromUtf8("imagefolder"))
        self.verticalLayout.addWidget(self.imagefolder)
        self.browseButton = QtWidgets.QPushButton(Dialog)
        self.browseButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  font-size: 14px;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"  color: #fff;\n"
"  background-color: #428bca;\n"
"  border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #3071a9;\n"
"  border-color: #285e8e;\n"
"}"))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.verticalLayout.addWidget(self.browseButton)
        self.progress = QtWidgets.QProgressBar(Dialog)
        self.progress.setStyleSheet(_fromUtf8("QProgressBar {\n"
"  border: 2px solid grey;\n"
"  border-radius: 5px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #3366FF;\n"
"  width: 10px;\n"
"  margin: 1px;\n"
"}"))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.verticalLayout.addWidget(self.progress)
        self.scoreButton = QtWidgets.QPushButton(Dialog)
        self.scoreButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  font-size: 14px;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"  color: #fff;\n"
"  background-color: #428bca;\n"
"  border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #3071a9;\n"
"  border-color: #285e8e;\n"
"}"))
        self.scoreButton.setObjectName(_fromUtf8("scoreButton"))
        self.verticalLayout.addWidget(self.scoreButton)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"  font-size: 14px;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 4px;\n"
"  color: #fff;\n"
"  background-color: #428bca;\n"
"  border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  color: #fff;\n"
"  background-color: #3071a9;\n"
"  border-color: #285e8e;\n"
"}"))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.subscriptionkey, self.imagefolder)
        Dialog.setTabOrder(self.imagefolder, self.browseButton)
        Dialog.setTabOrder(self.browseButton, self.scoreButton)
        Dialog.setTabOrder(self.scoreButton, self.closeButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.subscriptionkey.setPlaceholderText(_translate("Dialog", "Subscription Key", None))
        self.imagefolder.setPlaceholderText(_translate("Dialog", "Image Folder", None))
        self.browseButton.setText(_translate("Dialog", "Browse", None))
        self.scoreButton.setText(_translate("Dialog", "Score", None))
        self.closeButton.setText(_translate("Dialog", "Close", None))

