# -*- encoding: utf-8 -*-

import logging
from PyQt5.QtWidgets import QDialog
from .Ui_SettingsDialog import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    APP_NAME = 'TCP Client App'

    def __init__(self, parent=None):
        super().__init__(parent)
        super(Ui_SettingsDialog).__init__()
        self.lineEdit = None  # IP address string
        self.spinBox = None  # Port
        self.buttonBox = None  # OK / Cancel
        self.setupUi(self)
        self.lineEdit.textEdited.connect(self.check_sever_address)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def check_sever_address(self):
        logging.debug('Checking whether sever_address is valid...')
        logging.debug(self.lineEdit.text())

    @staticmethod
    def getAllSettings(server_address: str = '127.0.0.1', port: int = 8080, parent=None):
        dialog = SettingsDialog(parent)
        dialog.lineEdit.setText(server_address)
        dialog.spinBox.setValue(port)
        all_settings = {
            'sever_address': server_address,
            'port': port
        }
        result = dialog.exec_()
        all_settings['sever_address'] = dialog.lineEdit.text()
        all_settings['port'] = dialog.spinBox.value()
        return all_settings, QDialog.Accepted == result
