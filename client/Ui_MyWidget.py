# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MyWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyWidget(object):
    def setupUi(self, MyWidget):
        MyWidget.setObjectName("MyWidget")
        MyWidget.resize(400, 300)
        self.vBox = QtWidgets.QVBoxLayout(MyWidget)
        self.vBox.setContentsMargins(1, 1, 1, 1)
        self.vBox.setObjectName("vBox")
        self.textEdit = QtWidgets.QTextEdit(MyWidget)
        self.textEdit.setStyleSheet("background-color: transparent;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.vBox.addWidget(self.textEdit)
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.setObjectName("hBox")
        self.lineEdit = QtWidgets.QLineEdit(MyWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.hBox.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(MyWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.hBox.addWidget(self.pushButton)
        self.vBox.addLayout(self.hBox)

        self.retranslateUi(MyWidget)
        QtCore.QMetaObject.connectSlotsByName(MyWidget)

    def retranslateUi(self, MyWidget):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setPlaceholderText(_translate("MyWidget", "Enter command here..."))
        self.pushButton.setText(_translate("MyWidget", "Send"))

