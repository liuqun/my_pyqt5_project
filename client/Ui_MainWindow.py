# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/qt-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/images/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon2)
        self.actionConnect.setObjectName("actionConnect")
        self.actionEditSettings = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionEditSettings.setIcon(icon3)
        self.actionEditSettings.setObjectName("actionEditSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionEditSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionEditSettings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My TCP Client App"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionConnect.setToolTip(_translate("MainWindow", "Connect to server / disconnect from server"))
        self.actionEditSettings.setText(_translate("MainWindow", "&Settings..."))
        self.actionEditSettings.setToolTip(_translate("MainWindow", "Edit connection settings"))
        self.actionAbout.setText(_translate("MainWindow", "&About..."))
        self.actionAbout.setToolTip(_translate("MainWindow", "About this program"))

import client_app_rc
