# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MyCentralWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyCentralWidget(object):
    def setupUi(self, MyCentralWidget):
        MyCentralWidget.setObjectName("MyCentralWidget")
        MyCentralWidget.resize(400, 309)
        self.vBox = QtWidgets.QVBoxLayout(MyCentralWidget)
        self.vBox.setContentsMargins(1, 1, 1, 1)
        self.vBox.setObjectName("vBox")
        self.videoWidget = QVideoWidget(MyCentralWidget)
        self.videoWidget.setMinimumSize(QtCore.QSize(0, 240))
        self.videoWidget.setObjectName("videoWidget")
        self.vBox.addWidget(self.videoWidget)
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.setObjectName("hBox")
        self.pushButton = QtWidgets.QToolButton(MyCentralWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.hBox.addWidget(self.pushButton)
        self.pauseButton = QtWidgets.QToolButton(MyCentralWidget)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setObjectName("pauseButton")
        self.hBox.addWidget(self.pauseButton)
        self.horizontalSlider = QtWidgets.QSlider(MyCentralWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.hBox.addWidget(self.horizontalSlider)
        self.vBox.addLayout(self.hBox)
        self.label = QtWidgets.QLabel(MyCentralWidget)
        self.label.setObjectName("label")
        self.vBox.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(MyCentralWidget)
        self.label_2.setObjectName("label_2")
        self.vBox.addWidget(self.label_2)

        self.retranslateUi(MyCentralWidget)
        QtCore.QMetaObject.connectSlotsByName(MyCentralWidget)

    def retranslateUi(self, MyCentralWidget):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MyCentralWidget", "Play"))
        self.pauseButton.setText(_translate("MyCentralWidget", "Pause"))
        self.label.setToolTip(_translate("MyCentralWidget", "当前视频文件名"))
        self.label.setText(_translate("MyCentralWidget", "000"))
        self.label_2.setText(_translate("MyCentralWidget", "TextLabel"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
