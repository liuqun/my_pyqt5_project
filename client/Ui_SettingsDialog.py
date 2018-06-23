# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(300, 240)
        self.verticalLayoutWidget = QtWidgets.QWidget(SettingsDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 300, 240))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConnectionSettings = QtWidgets.QWidget()
        self.tabConnectionSettings.setAccessibleName("")
        self.tabConnectionSettings.setObjectName("tabConnectionSettings")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabConnectionSettings)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 251, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblSeverAddr = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSeverAddr.setObjectName("lblSeverAddr")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSeverAddr)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lblSeverPort = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSeverPort.setObjectName("lblSeverPort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblSeverPort)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(65535)
        self.spinBox.setProperty("value", 9999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.tabWidget.addTab(self.tabConnectionSettings, "")
        self.tabOtherSettings = QtWidgets.QWidget()
        self.tabOtherSettings.setObjectName("tabOtherSettings")
        self.tabWidget.addTab(self.tabOtherSettings, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.tabConnectionSettings.setToolTip(_translate("SettingsDialog", "Settings"))
        self.lblSeverAddr.setText(_translate("SettingsDialog", "Sever address:"))
        self.lineEdit.setText(_translate("SettingsDialog", "127.0.0.1"))
        self.lblSeverPort.setText(_translate("SettingsDialog", "Port:"))
        self.spinBox.setToolTip(_translate("SettingsDialog", "Port number from 1 to 65535"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnectionSettings), _translate("SettingsDialog", "Network"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOtherSettings), _translate("SettingsDialog", "Other"))

