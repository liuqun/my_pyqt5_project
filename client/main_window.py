# -*- encoding: utf-8 -*-

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .my_widget import MyWidget
from .settings_dialog import SettingsDialog
from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    COMPANY_NAME = '青岛中瑞电科'
    APP_NAME = 'TCP Client App'

    def __init__(self):
        super().__init__()
        super(Ui_MainWindow).__init__()
        self.toolBar = None
        self.actionConnect = None
        self.centralWidget = None
        self.setupUi(self)
        self.actionEditSettings.triggered.connect(self.show_settings_dialog)
        self.actionConnect.triggered.connect(self.on_action_connect_triggered)
        self.myWidget = MyWidget()
        self.myWidget.sock.disconnected.connect(self.on_connection_lost)
        self.setCentralWidget(self.myWidget)

    def getCurrentSettings(self):
        qs = QSettings(self.COMPANY_NAME, application=self.APP_NAME)
        sever_address = qs.value('sever_address', 'localhost', type=str)
        port = qs.value('port', 9999, type=int)
        del(qs)
        return sever_address, port

    def saveSettings(self, sever_address: str, port: int):
        qs = QSettings(self.COMPANY_NAME, application=self.APP_NAME)
        qs.setValue('sever_address', sever_address)
        qs.setValue('port', port)
        del(qs)

    def on_action_connect_triggered(self):
        if self.myWidget.isConnectedToServer:
            self.myWidget.disconnect()
            return
        sever_address, port = self.getCurrentSettings()
        try:
            self.myWidget.connect(sever_address, port)
        except ConnectionError as e:
            self.actionConnect.setChecked(False)
            msg = str(e)
            QMessageBox.critical(self, 'Error', msg)
            self.myWidget.add_message(msg + '\n')
            self.actionEditSettings.setEnabled(True)
            return
        self.actionEditSettings.setEnabled(False)

    def on_connection_lost(self):
        self.actionConnect.setChecked(False)
        self.actionEditSettings.setEnabled(True)

    def show_settings_dialog(self):
        sever_address, port = self.getCurrentSettings()
        all_settings, ok = SettingsDialog.getAllSettings(sever_address, port, self)
        if ok:
            sever_address = all_settings['sever_address']
            port = all_settings['port']
            self.saveSettings(sever_address, port)
